
import json
Emp = '''
{
"Employees" : [
{
"userId":"rirani",
"jobTitleName":"Developer",
"firstName":"Romin",
"lastName":"Irani",
"preferredFullName":"Romin Irani",
"employeeCode":"E1",
"region":"CA",
"phoneNumber":"408-1234567",
"emailAddress":"romin.k.irani@gmail.com"
},
{
"userId":"nirani",
"jobTitleName":"Developer",
"firstName":"Neil",
"lastName":"Irani",
"preferredFullName":"Neil Irani",
"employeeCode":"E2",
"region":"CA",
"phoneNumber":"408-1111111",
"emailAddress":"neilrirani@gmail.com"
},
{
"userId":"thanks",
"jobTitleName":"Program Directory",
"firstName":"Tom",
"lastName":"Hanks",
"preferredFullName":"Tom Hanks",
"employeeCode":"E3",
"region":"CA",
"phoneNumber":"408-2222222",
"emailAddress":"tomhanks@gmail.com"
}
]
}
'''
print(type(Emp))
#converting into python readable string format
data = json.loads(Emp)
for each in data['Employees']:
	del each['region']
#converting backt o json string format
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

