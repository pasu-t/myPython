def doormat(x,y):
   for i in range(x):
      if i < int(x/2):
         l1 = len('.|.'*(2*i+1)) #multiply odd number of times
         l2 = int((y-l1)/2)
         line = '-'*l2 + '.|.'*(2*i+1) + '-'*l2
      if i == int(x/2):
         l3 = int((y-len('WELCOME'))/2)
         line = '-'*l3 + 'WELCOME' + '-'*l3
      if i > int(x/2):
         # print(i,(2*(x-i-1)+1))
         l4 = len('.|.'*(2*(x-1-i)+1))
         l5 = int((y-l4)/2)
         line = '-'*l5 + '.|.'*(2*(x-1-i)+1) + '-'*l5

      print(line)

doormat(11,55)