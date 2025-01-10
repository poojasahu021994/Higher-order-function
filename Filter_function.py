my_tuple=(70,75,60,59,40,60,80)
def grater (x):
    if x>60:
        return x
x=list(filter(grater,my_tuple))
print(x)        
