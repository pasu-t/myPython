import sys
import robot_xml_parser as robot_par
import jira_mod

jira_obj = jira_mod.jiralib()

def get_previous_jira(label = None):
	'''
	filter the issue in jira database based on the labels and returns jira id.

    *Parameters:* label is list of labels that is unique to each issue. Based on these labels, it will filter issues.

    *Return:* Returns jira ID if issue is found or else it will return None

	'''
	if label is not None:
		# print('status not in (closed) AND labels = {} AND labels = {} AND labels = {}'.format(*label))
		old_jira = jira_obj.query_jira('status not in (closed) AND labels = {} AND labels = {} AND labels = {}'.format(*label))

		if len(old_jira) > 1:
			print('Error: Seen more than one issue with the given labels.Manually update single issue with the failed suites and close duplicate issues ')
			exit()
		elif old_jira:
			print('Existing issue found in JIRA: ', str(old_jira[0].key))
			return str(old_jira[0].key)                           
		else:
			return None

def create_new_jira(summary, description, partnumber,build, label=None):
	'''
	This is a method for creation of customized JIRA for ONT product.It just creates an issue with the fields given and return it's jira ID
    
    *Parameters:* 
    | *Key*               | *Value*                                   |
    |  *summary*          | Summary of the issue                      |
    |  *description*      | Description of the issue 			      |
    |  *partnumber*       | part number of the unit                   |
    |  *build*            | build version of the unit                 |
    |  *label*            | list of labels. This is must need identify the issue and to update the issue in future |

    *Return:*  jira ID of the created issue

	'''
	if all([summary, description, partnumber, build, label]) :
		issue_dict = {
		"project"    				: {"key": "ABCD"},
		"issuetype"                 : {"name": "Bug"},
		"summary"					: summary,
		"description"               : description,
		"components"                : [{"name" : "QA"}],
		"priority"					: {"name" : "Major"},
		"customfield_10363"         : partnumber,
		"customfield_10011"         : build,
		"customfield_10012"         : {"value": "System Test"},
		"customfield_10015"         : {"value" : "Create On Demand"},
		"labels"                    : label
		}

		new_jira = jira_obj.create_jira(issue_dict=issue_dict)
		return new_jira

	else:
		print('Error: Unable to create jira as some mandatory fields are not filled')

def auto_jira_handler(log_folder,partnumber,platform,build):
	'''
	This method will handle the process of automatic issue creation and updation.
	steps:
	-> It parses the robot output xml file and divides the failed and passed suites.
	-> Then for failed suites it will check if any previuosly created issues
	-> If any previous issue found, then will just comment with more info and attach the required log files.
	-> If no previous issue found, then call create_new_jira() method. And then attaches the required log for new issue
	-> Then for passed suites, it will check if any previuosly created issues
	-> If any previous issue found, it will just attach the required log and closes that issue
    
    *Parameters:* 
    | *Key*               | *Value*                                   |
    |  *log_folder*       | path to robot logs                        |
    |  *partnumber*       | part number of the unit                   |
    |  *platform*         | unit(ONT) flavour                         |
    |  *build*            | build version of the unit                 |

    *Return:* None

	'''

	log_html = log_folder + build + '_log.html'
	output_xml = log_folder + build + '_output.xml'
	try:
		stats = robot_par.get_stats(output_xml)
	except Exception as e:
		print(e)
		exit()

	if stats['failed_suites']:

		print('found failed suites')
		# print(stats['failed_suites'])

		for each in stats['failed_suites']:
			flabel = ['ONT_CI_PIPELINE', list(each.keys())[0].name.replace(" ", "_"), platform]
			prev_jira = get_previous_jira(flabel)
			if prev_jira is not None:
				print('trying to update existing issue', prev_jira)
				add_comment = '\n' + 'build version: '+ build + '\n' + 'Failed Tests:\n'
				for test in list(each.values())[0]:
					if test[1] == 'FAIL':
						add_comment += '|' + test[0] + '|' + "".join([s for s in str(test[2]).strip().splitlines(True) if s.strip()]) +'|' + '\n'
				# print(add_comment)
				jira_obj.update_jira(jira_id = prev_jira, comment = add_comment)
				jira_obj.update_jira(jira_id = prev_jira, attachment = log_html)
			else:
				print('Creating new issue on jira')
				summary = 'ONT_CI_JIRA : ' + platform + ' ' + list(each.keys())[0].name + ' Failed'
				description = 'Unit Under Test: ' + platform  + '\n' + 'suite: ' + list(each.keys())[0].name + '\n\n' +\
							  'For detailed information refer tables in comment section.\n' +\
							  'column1 gives list of testcases and column2 gives their failure reason' 
				first_comment = 'build version: '+ build + '\n' + 'Failed tests : ' + '\n'
				for test in list(each.values())[0]:
					if test[1] == 'FAIL':
						first_comment += '|' + test[0] + '|' + "".join([s for s in str(test[2]).strip().splitlines(True) if s.strip()]) +'|' + '\n'
				# print(summary)
				# print(description)
				# print(first_comment)
				new_jira_id = create_new_jira(summary=summary, description=description, partnumber=partnumber, build= build, label = flabel)
				jira_obj.update_jira(jira_id = new_jira_id, comment = first_comment)
				jira_obj.update_jira(jira_id = new_jira_id, attachment = log_html)
	else:
		print('no failed suites were found')

	if stats['passed_suites']:
		print('found passed_suites')
		# print(stats['passed_suites'])

		for each in stats['passed_suites']:
			plabel = ['ONT_CI_PIPELINE', list(each.keys())[0].name.replace(" ", "_"), platform]
			prev_jira2 = get_previous_jira(plabel)
			if prev_jira2 is not None:
				print('trying to close previous jira', prev_jira2)
				jira_obj.update_jira(jira_id = prev_jira2, attachment = log_html)
				close_comment = 'Issue have been closed automatically by pipeline.It got resolved in build version: ' + build
				jira_obj.close_jira(prev_jira2, comment=close_comment)			
	else:
		print('no passed suites were found')

if __name__ == '__main__':

	auto_jira_handler(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	
	# example: ont_auto_jira.py C:\\Users\\pthumbur\\Desktop\\temp\\automatic_issue_creation\\logs\\ 1287781F2 424XRG build1