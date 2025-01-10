greet=lambda:print('Hello world')
greet()

x=lambda a,q,r:3*a+4*q+5*r+5
print(x(10,20,30))

my_list={12,20,10,5}
y=list(map(lambda x : x*2,my_list))
print(y)
