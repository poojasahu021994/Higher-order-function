# my_list=[10,50,23,46,11,78,51,20]
# x=list(filter(lambda x:x%2==0,my_list))
# print(x)

import functools
# my_list1=[10,50,23,46,11,78,51,20,30,55]
# x=filter(lambda x:x%2==0,my_list)
# y=functools.reduce(lambda x,y: x+y ,x)
# print(y)

# from functools import reduce
# my_list1=[10,50,23,46,11,78,51,20,30,55]
# x=filter(lambda x:x%2==0,my_list)
# y=reduce(lambda x,y: x+y ,x)
# print(y)

# square even number addition
# import functools
# my_list=[10,50,23,46,11,78,51,20,30,55]
# even_data=list(filter(lambda x:x%2==0,my_list))
# even_squer=list(map(lambda x:x**2,even_data))
# squer_sum=functools.reduce(lambda x,y: x+y ,even_squer)
# print(even_data)
# print(even_squer)
# print(squer_sum)

# even number --> even number sum-->sum squre
import functools
my_list=[10,50,23,46,11,78,51,20,30,55]
even_data=list(filter(lambda x:x%2==0,my_list))
even_number_sum=functools.reduce(lambda x,y: x+y ,even_data)
even_sum_squer=list(map(lambda x:x**2,even_number_sum))

print(even_data)
print(even_number_sum)
print(even_sum_squer)
