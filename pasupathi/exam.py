qp = open('question_paper.txt', 'r').readlines()
qp = list(map(lambda s: s.strip(), qp))
for each in qp:
    if each == '':
        qp.remove(each)
questions = qp[::2]
answers = []
for each in qp[1::2]:
    answers.append(each.split(','))

for i in answers:
    i = dict(zip(['a', 'b', 'c', 'd'], i))

print(answers)

#qp_dict = dict(zip(questions, answers))
#print(qp_dict)
keys = ['c', 'b', 'a', 'b']


score = 0
'''
for count, ele in enumerate(qp_dict.keys(), 1):
    print(count, ele)
    print(qp_dict[ele])
    '''
