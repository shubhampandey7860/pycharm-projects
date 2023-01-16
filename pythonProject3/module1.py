#  reuseable module
# non executable module
x=10
y=20
def fun1():
    print(f'fun1 of module1')
def fun2():
     print(f'fun2 of module1')
def fun3():
     print(f'fun3 of module1')


# # d=[]
# # a={3:'Three',2:'Two',1:"one"}
# # for i in a.values():
# #     d.append(i)
# # d.sort(reverse=True)
# # # print(d)
# #
# # vowel=[]
# # consonent=[]
# # x = input()
# # for i in x:
# #     if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u') or (
# #         i == 'A' or i == 'E' or i== 'I' or i == 'O' or i == 'U'):
# #         vowel.append(i)
# #
# #
# #     else:
# #        consonent.append(i)
# #
# # print(f'vowel list:{vowel}')
# # print(f'consonent list:{consonent}')
# # #
# # _=input()
#
# #
# def convertString(String):
#     c=[]
#
#     b=String.split()
#     for i in b:
#          b=i.capitalize()
#          c.append(b)
#     R=' '.join(c)
#     return R
#
# for i in range(3):

#     print(convertString(input()))
#
#
#
#
#
#
#
#
#
#
#
#
#

# def convertString(str):
#     str = list(str)
#
#     # Check if first character is small
#     if str[0] >= 'a':
#         str[0] = str[0].upper()
#
#     for i in range(1, len(str)):
#         # For all the characters following a space, make them capital
#         if str[i-1] == ' ' and str[i] >= 'a':
#             str[i] = str[i].upper()
#
#     # Return the final answer
#     return str
# print(convertString("shubHam pandey chodu"))
# n=input('enter character:')
# if n >= 'a' and n <= 'z':
#     print('small letter')
# elif n>='A' and n<='Z':
#     print('capital letter')
# else:
#     print('special symbol')
i=1
n=3
while i<11:
    if i%2==0:
        print(f'{3}*{i}={3*i}')
    elif i==1:
        print(f'{3}*{i}={3*i}')
    i+=1


