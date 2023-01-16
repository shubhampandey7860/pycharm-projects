# # importing module1 here

import module1

#
def main():
    module1.fun1()  # here we are calling fun1 of module1
    module1.fun2()  # here we are calling fun2 of module1
    module1.fun3()  # here we are calling fun3 of module1


main()

# import module1 as m1  # aliasing module name
import module1 as m1
def main():
     m1.fun1()
     m1.fun2()
     m1.fun3()
     print(f'value of x:{m1.x}')
     print(f'value of y:{m1.y}')


main()

# # from moduleName import *

from module1 import *
def main():
     fun1()
     fun2()
     fun3()
     print(f'value of x:{x}')
     print(f'value of y:{y}')
main()
#
# # from moduleName import identifier,identifier
# import module1
# from module1 import x,y
# def main():
#     print(f'value of x:{x}')
#     print(f'value of y:{y}')
#     module1.fun1()
# main()
#
# #
# class A:
#     def m1(self):
#         print(f'm1 method of class A')
#     def m2(self):
#         print(f'm2 method of class A')
# class B(A):
#     def m3(self):
#         print(f'm3 method of class B')
#     def m4(self):
#         print(f'm4 method of class B')
# #
# c=0
# n=input('enter number:')
# b=int(n)
# for i in n:
#     b//=10
#     c+=1
# print(f'count of digit:{c}')

#
# removing duplicates
T=''
n=input('enter string:')
for i in n:
    if i not in T:
        T=T+i
print(T)

# reverse given string without slicing
T=''
n=input('enter string:')
for i in range(-1,-len(n)+1,-1)):
    T=T+i
print(f'{n}:{T}')
