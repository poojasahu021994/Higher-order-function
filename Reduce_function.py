#import functools
from functools import reduce
my_tuple =(10,20,30,40,50)
def max_digit(x,y):
    if x>y:
        return 
    else:
        return y
x =reduce(max_digit,my_tuple)
print(x)    


#2nd import function use
import functools
my_tuple =(10,20,30,40,50)
def max_digit(x,y):
    if x>y:
        return 
    else:
        return y
x =functools.reduce(max_digit,my_tuple)
print(x)    
