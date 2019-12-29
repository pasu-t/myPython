import os
import time
import tempfile
from bs4 import BeautifulSoup
from itertools import chain


class NessusGui():
	"""
	Library for configuring services and various features on Nessus tool web interface.
	"""

	def __init__(self):
		super(NessusGui, self).__init__()
		try:
			from robot.libraries.BuiltIn import BuiltIn
			log_dir = BuiltIn().replace_variables('${OUTPUT_DIR}')
		except:
			log_dir = tempfile.gettempdir()
		self.download_path = log_dir.replace('\\', '//') + '//saved_scans//'
		if not os.path.exists(self.download_path):
			os.makedirs(self.download_path)
		# else:
		# 	for file in os.listdir(self.download_path):
		# 		os.remove(self.download_path+'//'+file)

	def _go_to_dashboard(self):
		self.any_condition_wait('class=logo', 10, condition="element_to_be_clickable")
		self.force_click('class=logo')
		time.sleep(1)

	def _force_click_on_text(self, text, timeout=2):
		if isinstance(text, str):
			text_xpath = "//*[contains(text(), '" + text + "')]"
			try:
				xpath = 'xpath='+text_xpath
				self.any_condition_wait(xpath, timeout=10)
				element = self.browser.find_element_by_xpath(text_xpath)
				self.force_click(element)
				time.sleep(timeout)
			except:
				raise AssertionError('Unable to find text %s' % text)
		elif isinstance(text, list):
			for label in text:
				text_xpath = "//*[contains(text(), '" + label + "')]"
				try:
					xpath = 'xpath=' + text
					self.any_condition_wait(xpath, timeout=10)
					element = self.browser.find_element_by_xpath(text_xpath)
					print '*************',element
					self.force_click(element)
					time.sleep(timeout)
				except:
					raise AssertionError('Unable to find text %s' % label)

	def _go_to_folder(self, side_menu_folder, folder_path=None):
		self.any_condition_wait('tag=ul', timeout=10)
		side_menu = self.element_find('tag=ul')
		for folder in side_menu.find_elements_by_css_selector('li a'):
			if side_menu_folder in folder.text.strip():
				self.force_click(folder)
				break
		if folder_path:
			placeholder = 'Search Scans'
			self.textinput_set("xpath=//input[@placeholder='" + placeholder + "']", folder_path[0])
			for folder in folder_path:
				self._force_click_on_text(folder)

	def _table_get(self, index_to_delete=None):
		return_list = []
		# Capturing header details
		thead = [header.lower().replace(' ', '_') for header in list(filter(None, self.execute_script('return [...document.querySelectorAll("tr th")].map(e=>e.textContent)')))[1:]]
		# Capturing table body details
		tbody = [data.strip() for data in list(filter(None, self.execute_script('return [...document.querySelectorAll("tr td")].map(e=>e.textContent)')))]
		unicode_flag = False
		for row in tbody:
			if isinstance(row, unicode):
				unicode_flag = True
				break

		# Removing empty unicode characters and table numeric codes
		if unicode_flag:
			tbody_copy = []
			for item in tbody:
				if isinstance(item, unicode):
					if item == u'' or item.isdigit():
						continue
					else:
						tbody_copy.append(str(item))
			tbody = tbody_copy

		# Removing items at specific index (Optional)
		if index_to_delete:
			del tbody[::index_to_delete]

		# Breaking tbody into equal chunks
		tbody = [tbody[i:i + len(thead)] for i in range(0, len(tbody), len(thead))]

		# Formulating list of dictionaries, where eavh dictionary is a table row
		for data in tbody:
			return_list.append(dict(zip(thead, data)))
		return return_list

	def launch_scan(self, scan_name):
		"""
		This method navigates to All Scans menu option, selects and launches a scan.

		*Parameters*:

		- *scan_name* : <string> ; Name of the scan.

		*Returns* : None
		"""
		try:
			self._go_to_folder('All Scans', folder_path=[str(scan_name), 'Launch', 'Default'])
			time.sleep(2)
		finally:
			self._go_to_dashboard()

	def scan_status_get(self, scan_name):
		"""
		This method navigates to All Scans->*scan_name*->History and returns the latest scan status.

		*Parameters*:

		- *scan_name* : <string> ; Name of the scan.

		*Returns* : Scan status <completed/cancelled/running>
		"""
		try:
			self._go_to_folder('All Scans', folder_path=[str(scan_name), 'History'])
			table_data = self._table_get()
			if len(table_data) > 0:
				return table_data[0]['status']
			else:
				raise AssertionError('History table is empty')
		finally:
			self._go_to_dashboard()

	def wait_until_scan(self,scan_name):
		"""
		This method waits until the scan with *scan_name* is completed.

		*Parameters*:

		- *scan_name* : <string> ; Name of the scan.

		*Returns* : None

		"""
		wait_time = 0
		while True:
			time.sleep(60)
			wait_time += 1
			if self.scan_status_get(str(scan_name)) == 'completed':
				break
			elif wait_time == 30:
				print('Scanning is taking longer than usual. Please check the environment')

	def export_scan(self, scan_name):
		try:
			self._go_to_folder('All Scans', folder_path=[str(scan_name), 'History'])
			table_data = self._table_get()
			if len(table_data) > 0:
				if table_data[0]['status'].lower().strip() == 'completed':
					row_element =  self.element_find('tag=tr')
					self.force_click(row_element)
					check_box_element = self.element_find('class=checkbox')
					self.force_click(check_box_element)
					self.force_click('id=export')
					self._force_click_on_text('HTML')
					self.force_click('id=export-save')
					time.sleep(10)
					try:
						while 'exporting' in self.element_find('id=export_save').text.lower():
							time.sleep(10)
							continue
					except:
						pass
					print '#################################'
					print 'Scan report saved path: %s' % self.download_path.replace('//', '\\')
					print '#################################'
			else:
				raise AssertionError('History table is empty')
		finally:
			self._go_to_dashboard()

	def get_filename(self, scan_name): 
		"""
		This method filters the scan report name from the scan reports folder.

		*Parameters*:
		- *scan_name* : <string> ; Name of the scan.

		*Returns* : returns the filename of the report for the given scan

		"""

		try:
			mylist=os.listdir(self.download_path.replace('//', '\\'))
			print(mylist)
			for each in mylist:
				if each.startswith(str(scan_name)):
					return each
		except:
			raise AssertionError('Error while getting the filename of scan report')


	def nessus_html_parser(self, nessus_html_report):
		"""
		This method opens a saved scan report and returns the statistics.
	`
		*Parameters*:
		- *nessus_html_report* : <string> ; Path of the exported scan report.

		*Returns* : List of dictionaries, each dictionary containing IP address and criticalitis.

		"""
		soup = None
		try:
			with open(self.download_path + '\\' + nessus_html_report) as html_file:
				soup = BeautifulSoup(html_file, 'lxml')
		except IOError:
			raise AssertionError('Check the html report. Unable to find the file for parsing the results')
		if soup is not None:
			crit_list, high_list, med_list, low_list, info_list, vuln_list = [], [], [], [], [], []
			for vuln_crit in soup.find_all('td', class_='#d43f3a'):
				crit_list.append({'critical' : vuln_crit.text.encode('utf-8')})
			for vuln_high in soup.find_all('td', class_='#ee9336'):
				high_list.append({'high' : vuln_high.text.encode('utf-8')})
			for vuln_med in soup.find_all('td', class_='#fdc431'):
				med_list.append({'medium' : vuln_med.text.encode('utf-8')})
			for vuln_low in soup.find_all('td', class_='#3fae49'):
				low_list.append({'low': vuln_low.text.encode('utf-8')})
			for vuln_info in soup.find_all('td', class_='#0071b9'):
				info_list.append({'info' :vuln_info.text.encode('utf-8')})

			ip_info = soup.find('li').text.encode('utf-8').split('\n')
			if len(ip_info) == 3:
				ip_list = [ip_info[1].split('y')[1]]
			else:
				ip_list = ip_info[2:-2]
			for vuln in map(lambda a,b,c,d,e : [a,b,c,d,e], crit_list, high_list, med_list, low_list, info_list):
				vuln_list.append(dict(chain.from_iterable(d.iteritems() for d in (vuln[0], vuln[1], vuln[2], vuln[3], vuln[4]))))
			ret_list = map(lambda a,b : {a : b},ip_list,vuln_list)

			return ret_list

	def vuln_count(self, list_report, ip_addr):

		try:
			return int(list_report[0][str(ip_addr)]['critical']) + int(list_report[0][str(ip_addr)]['high']) + int(list_report[0][str(ip_addr)]['medium']) + int(list_report[0][str(ip_addr)]['low'])
		except KeyError:
			raise AssertionError('Unable to get details for the given ip address ' + ip_addr)




