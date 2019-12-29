import sys
import os
import selenium.webdriver.remote.webelement
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from taut_selenium import TautSelenium
from taut_nessus.command.nessus_gui import NessusGui
import time


class NessusWeb(NessusGui, TautSelenium, object):
    def __init__(self):
        super(NessusWeb, self).__init__()

    def login(self, nessus_ip, username='Adtran', password='Adtran1234', browser_type='gc', driver_path=None,
              download_path=None):
        """
        Log into the browser as specified with parameters

        *Parameters:*
        | *Key*               | *Value*                                 |
        |  *nessus_ip*        | Nessus server IP address                |
        |  username           | Username for login, default is Adtran   |
        |  password           | Password for login, default is Adtran1234   |
        |  browser_type       | Browser type, valid values: <FF|IE|GC> FF: Firefox, IE : Internet explorer GC: Google chrome,Default FF  |
        |  driver_path        | Path to the web driver executable (for IE or Chrome). This parameter is ignored for Firefox. |
        |  download_path      | Path to the location where files should be downloaded. If none is provided, this will default \
                        to the TAUT selenium communication library's directory  |

        *Return:* None

        Examples:
        | Login | nessus_ip = ${nessus_ip} |
        | Login | nessus_ip = ${nessus_ip} | username = ${username} | password = ${password} |

        """
        if not nessus_ip:
            raise AssertionError('Nessus IP has not been defined')

        browser_id = self.browser_open(browser_type, driver_path, download_path)

        url = ('%s' % (nessus_ip))
        self.browser_get(url)

        # Login
        self.textinput_set("xpath=.//*[@class='login']/div[1]/input", username)
        self.textinput_set("xpath=.//*[@class='login']/div[2]/input", password)
        self.force_click('tag=button')

    def browser_open(self, browser_type='firefox', driver_path=None, download_path=None):
        """
        Opens web browser.

        *Parameters:*
        | *Key*               | *Value*                                                                      |
        |  browser_type       | Browser type, valid values: <FF|IE|GC> FF: Firefox, IE : Internet explorer GC: Google chrome,Default FF  |
        |  driver_path        | Path to the web driver executable (for IE or Chrome). This parameter is ignored for Firefox.    |
        |  download_path      | Path to the location where files should be downloaded. If none is provided, this will default \
                        to the TAUT selenium communication library's directory     |

        *Return:* Open object for the web driver.

        Examples:
        | Browser Open |                                |                            |
        | Browser Open | browser_type = ${browser_name} |                            |
        | Browser Open | browser_type = ${browser_name} | driver_path=${driver_path} | download_path=${download_path} |
        """

        # check for system variable TAUT_CORE
        script_path = 'C:\\Python27\\Lib\\site-packages\\taut_selenium'
        default_ie_driver_path = '%s\\IEDriverServer.exe' % script_path
        default_chrome_driver_path = '%s\\chromedriver.exe' % script_path
        if download_path is None:
            download_path = script_path

        # check for requested browser type
        # IE
        if browser_type.lower() in ['ie', 'internetexplorer']:
            # IE is always windows, no OS check required
            if not driver_path:
                driver_path = default_ie_driver_path

            # open IE
            self._browser = webdriver.Ie(executable_path='%s' % driver_path)
            self._browserType = 'ie'

        # Chrome
        elif browser_type.lower() in ['gc', 'chrome']:
            self.browser_type = 'chrome'
            chromeOptions = webdriver.ChromeOptions()
            prefs = {"download.default_directory": self.download_path.replace('//', '\\')}
            chromeOptions.add_experimental_option("prefs", prefs)
            # LINUX
            if sys.platform not in ['win32', 'win64', 'cygwin']:
                self.browser = selenium.webdriver.Chrome(chrome_options=chromeOptions)
            # WINDOWS
            else:
                if not driver_path:
                    driver_path = default_chrome_driver_path
                self.browser = selenium.webdriver.Chrome(executable_path=driver_path, chrome_options=chromeOptions)

        # Firefox
        elif browser_type.lower() in ['ff', 'firefox']:
            self.browser_type = 'firefox'
            #
            # TODO: do similar things for other web browsers

            profile = selenium.webdriver.FirefoxProfile()
            profile.set_preference('browser.download.folderList', 2)
            profile.set_preference(
                'browser.download.manager.showWhenStarting', False)
            profile.set_preference('browser.download.dir', "%s" % download_path)
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "*/*")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "config/conf")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                   "application/vnd.tcpdump.pcap,application/octet-stream,config/conf")
            profile.set_preference(
                'browser.helperApps.neverAsk.openFile', '*/*')
            profile.set_preference(
                'browser.helperApps.neverAsk.openFile', 'application/vnd.tcpdump.pcap,application/octet-stream')

            profile.set_preference('browser.helperApps.alwaysAsk.force', False)
            profile.set_preference(
                'browser.download.manager.showAlertOnComplete', False)
            profile.set_preference(
                'browser.download.manager.closeWhenDone', False)
            profile.set_preference('plugin.scan.plid.all', False)
            profile.set_preference('plugin.scan.Acrobat', '99.0')
            profile.set_preference('pdfjs.disabled', True)
            self.browser = webdriver.Firefox(profile)
            self.wait = WebDriverWait(self.browser, 10)
            self.browser.implicitly_wait(10)
            self.actions = webdriver.ActionChains(self.browser)
        # unknown browser
        else:
            raise AssertionError('Given Browser %s is not supported' % browser_type)

        self.browser.maximize_window()

        return self.browser

    def logout(self):
        """
        Logout from web page.

        *Parameters:* None

        *Return:* None
        """

        self.browser.switch_to.default_content()

        self.force_click(self.element_find('class=user-menu'))
        self._force_click_on_text('Sign Out')
        time.sleep(2)


if __name__ == '__main__':
    pass
    # ob = NessusWeb()
    # ob.login('https://10.49.143.200:8834')
    # ob.launch_scan('sample')
    # ob.wait_until_scan('sample')
    # ob.export_scan('sample')
    # filename = ob.get_filename('sample')
    # print ob.nessus_html_parser(filename)
    # ob.logout()
    # ob.browser_close()