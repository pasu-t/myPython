from jira.client import JIRA
options = {
    'server': 'https://jira.adtran.com'}
authed_jira = JIRA(basic_auth=('pthumbur', 'Kajal@143'), options = options)

myissue = authed_jira.issue('AD-135311')
transitions = authed_jira.transitions(myissue)
print(transitions)
authed_jira.transition_issue(myissue, '711')
