# import osw
from jira.client import JIRA

class jiralib:
	"""
	Library for creating and updating the issue on adtran jira database.
	"""
	def __init__(self):

		# password = os.environ.get('JIRA_PSWD')
		options = {
		    'server': 'https://jira.abcd.com'}
		self.jira = JIRA(basic_auth=('user', 'password'), options = options)

	def create_jira(self, issue_dict = None):
		'''
		This method creates new issue based on the given jira fields. Jira fields may vary depending on the project.

	    *Parameters:* issue_dict which should contian mandatory fields and their values in the form of dictionary. This dictionary will be used to create an issue.

	    *Return:* It returns the jira id of new issue which was created

		'''
		if issue_dict is not None:
			try:
				new_issue = self.jira.create_issue(fields=issue_dict)
				print('Issue created: ',  new_issue)
				return new_issue
			except Exception as e:
				print(e)

	def update_jira(self, jira_id, summary=None, description=None, attachment=None, comment = None):
		'''
		This method updates the issue which is limited to few fields of jira database like attachements, summary,descrption and comment.

		*Parameters:* 
	    | *Key*               | *Value*                                         |
	    | *jira_id*           | jira ID of the issue that needs to be updated   |
	    | *summary*           | New summary of the issue                        |
	    | *description*       | New description of the issue 			        |
	    | *Attachment*        | file/file path that needs to attached 			|
	    | *comment*           | Add comment										|

	    *Return:* None

		'''

		try:
			issue = self.jira.issue(jira_id)
			if attachment:
				self.jira.add_attachment(issue=issue, attachment=attachment)
			if summary:
				issue.update(summary=summary)
			if description:
				issue.update(description=description)
			if comment:
				issue.update(comment = comment)
			print('jira updated successfuly')
		except Exception as e:
			print(e)

	def close_jira(self, jira_id, comment):
		'''
		This method closes the issue based on the jira_id and its current status. If the issue is not allowed to close , then it will print an error.

				*Parameters:* 
	    | *Key*               | *Value*                                     |
	    | *jira_id*           | jira ID of the issue                        |
	    | *comment*           | comment that needs to added during updation |

	    *Return:* None

		'''

		issue = self.jira.issue(jira_id)
		transitions = self.jira.transitions(issue)
		list_transitions = list()
		for each in transitions:
			list_transitions.append(each['name'])
		print(list_transitions)
		if 'Close Issue' in list_transitions:
			try:
				self.jira.transition_issue(issue, 'Close Issue', comment = comment)
				print('Closed jira ' + jira_id + ' successfully')
			except Exception as e:
				print(e)
		else:
			print('Error: Unable to close the jira ' + jira_id)

	def query_jira(self, jql_str):
		'''
		This method returns the list of issues which are queried through jql

		*Parameters:* jql query in the form a string

	    *Return:* list of jira IDs of the issues which are queried through jql

		'''

		return self.jira.search_issues(jql_str)

	def get_description(self, jira_id):
		'''
		This method returns the description of the issue of jira ID

		*Parameters:* jira ID of the issue

	    *Return:* Description of the issue in string format

		'''

		return self.jira.issue(jira_id).fields.description

	def close_all_jira(self, jql_str):
		'''
		This method closes the list of issues which are queried through jql

		*Parameters:* jql query in the form a string

	    *Return:* None

		'''

		issues = self.jira.search_issues(jql_str)

		if issues:
			for issue in issues:
				close_jira(issue)

	def label_jira(self, jira_id, label = None):
		'''
		This method does label the issue. Currently "CN" project is not allowing to label affer creation of jira
		
		*Parameters:* 
	    | *Key*               | *Value*                                          |
	    | *jira_id*           | jira ID of the issue that needs to be labelled   |
	    | *label*             | label -> can be a single label or list of labels that can be appended to jira  |

	    *Return:* None

		Ex: label_jira('CN-13531', label = ['ONT_CI_HYD', 'BBB', '424'])

		'''
		if label:
			try:
				issue = self.jira.issue(jira_id)
				issue.update(fields={"labels": label})
				print('jira labelled successfuly')
			except Exception as e:
				print(e)

if __name__ == '__main__':
	x = jiralib()
	# x.close_jira('AB-58993', comment='something')