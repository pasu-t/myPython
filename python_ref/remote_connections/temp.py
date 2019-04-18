# import requests
# from jira.client import JIRA
# import urllib.request

# jira_server = "http://jira.adtran.com"
# jira_user = "vboyi"
# jira_password = "Password@1234"
import requests
username = 'vboyi'
password = 'Password@1234'
url = 'http://jira.adtran.com/rest/api/2/issue/465642/'
r = requests.get(url, auth=(username, password))  
page = r.content
print(page)
# group = jira.group_members("jira-users")
# for users in group:
#     print (users)