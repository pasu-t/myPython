import pandas as pd

tasks_list = [

{'Requester' : 'pasupathi',
'Task Summary' : 'Need python parser for the defenscics results',
'Task_Id' : 'AD-00000',
'Reward_Points' : 10,
'Date_Created' : 'Oct 20, 2019',},

{'Requester' : 'thumbur',
'Task Summary' : 'Optimize 4xx ONT framework',
'Task_Id' : 'AD-00001',
'Reward_Points' : 20,
'Date_Created' : 'Oct 21, 2019',}
]

df = pd.DataFrame(tasks_list)
print(df.to_html())