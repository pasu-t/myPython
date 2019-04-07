'''
import greet
greet.hello()
greet.bye()
print(greet.x)
#import greet as g #for shortcut
#g.hello()
'''
from greet import hello,party
#from greet import * #import all methods and variables
hello()
party()