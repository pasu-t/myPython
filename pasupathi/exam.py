qp = open('question_paper.txt', 'r').readlines()
qp = list(map(lambda s: s.strip(), qp))
for each in qp:
    if each == '':
        qp.remove(each)
questions = qp[::2]
answer = []
answers = []
for each in qp[1::2]:
    answer.append(each.split(','))
for i in answer:
    answers.append(dict(zip(['a', 'b', 'c', 'd'], i)))
keys = ('c', 'b', 'a', 'b', 'b')
score = 0
index = 0
qp_dict = dict(zip(questions, answers))
print(qp_dict)
for i, j in qp_dict.items():
    print(i)
    for m, n in j.items():
        print(m, '.', n)
    while True:
        ans = input('Enter option: ')
        if ans not in 'aAbBcCdD':
            print('Please enter valid input')
        else:
            break
    if ans == keys[index]:
        score += 1
    index += 1
print('your score is ', score)
