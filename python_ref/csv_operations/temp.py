import random
import sys
import os
import jira.client
import json
import logging
import datetime
import base64
import requests
import urllib
import smtplib
import re
from smtplib import SMTPException
# from win32com.client import Dispatch
# import win32com.client as win32
from jira.client import JIRA

"""
"project":{"key": "CN"},
"issuetype": {"name": "Bug"}},
"summary": "PI9 task for team Sherlock ",
"Component/s":"ONT - XGS-PON",
"Unit Part Number":"1287823F1",
"Version Found":"ML-720",
"description": "Creating of an task item to track",
"Priority":"Minor"
"Source":"System Test"
"Reproducibility":"Create On Demand"
===============
"project":{"key": "AD"},
"summary": "PI9-4 test jira for team Sherlock",
"description": str(failure_testcase_list),
"issuetype": {"name": "Story"}}
"""

#################Get the list of testcases failed to log.txt with team names and build ID#########
#http://172.22.49.180/api/build/56310/results

username = 'vboyi'
password = 'Password@1234'
#url=raw_input("Enter the skydocker URL")
url = 'http://172.22.49.180/api/build/56310/results'

def get_failed_tests(url):
	req = requests.get(url)
	with open("raw_data.txt","w") as file:
		file.write(req.text)
	with open("failed_testcases.txt","w") as file:
		with open("raw_data.txt","r") as file2:
			for line in file2.read().split('}'):
				if "fail" in line:
					p=re.search(r'"name":"[\s\S]+?"', line).group()
					q=re.search(r'"build_name":"[\s\S]+?"', line).group()
					r=re.search(r'"team_name":"[\s\S]+?"|"team_name":null', line).group()
					#print (p,q,r)
					file.write("{"),file.write(p),file.write(","),file.write(r),file.write(","),file.write(q),file.write("}"),file.write("\n")


###Get the list of testcase failures from log.txt#########
def display_failed_tests():
	p=open("failed_testcases.txt","r")
	lines = p.read()
	failure_testcase_list=re.findall(r'"name":"[\s\S]+?","team_name":[\s\S]+?"|null' ,lines)
	Build_ID=re.search(r'ML-[0-9]+', lines).group()

	print ("Failed testcases are " + str(failure_testcase_list))
	print ("Build_ID = " +Build_ID)
	return [failure_testcase_list,Build_ID]

###############Log bug in jira.adtran.com with all the failure testcases list##########
def create_jira(fail_tests_build):
	jira_options={"server":"http://jira.adtran.com/","verify":False}
	jira=JIRA(options=jira_options,basic_auth=("vboyi","Password@1234"))
	issue_dict = {
	"project":{"key": "AD"},
	"summary": "Solution fast run testcases in CI failed",
	"description": "Build ID = " +str(fail_tests_build[1]) +"\n"+str(fail_tests_build[0]),
	"issuetype": {"name": "Story"}}
	new_issue=jira.create_issue(fields=issue_dict,prefetch=True)
	print ("The rest API ID created is " +new_issue.id)
	return(new_issue.id)

def get_jira_id(new_issue_id):
	url = 'http://jira.adtran.com/rest/api/2/issue/'+ new_issue_id + '/'
	r = requests.get(url, auth=(username, password))  
	page = r.content
	JiraID = json.loads(page)
	print ("The jira ID created is " +JiraID['key'])

get_failed_tests(url)
failed_list_build = display_failed_tests()
new_issue_id = create_jira(failed_list_build)
get_jira_id(new_issue_id)



