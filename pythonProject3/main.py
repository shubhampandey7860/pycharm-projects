# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# a=266
# b=266
# print(id(a),id(b))
#
#
# a=[10,20,30,40]
# b=[10,20,30,40]
# print(id(a),id(b))
#
#
# #
# a=[11,12,13,14]
# c=int(str(a[2])+str(a[3]))
# a.remove(13)
# a.remove(14)
# print(a.append(c))
# print(a)
#
# #
# a=[11,12,13,14]
# a[2:]=[1314]print(a)
#
# #
# a={1:10,2:20,3:30,4:40}
# print(a.keys())
# print(a.values())
# print(a.items())




# #
# a=[0,1,0,1,0,1]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i] > a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

#
a=[0,1,0,1,0,1]
b=[]
for i in a:
    if i==0:
        b.insert(0,0)
    elif i==1:
        b.append(1)
print(b)

# debuge program
''' c=continue
    q=quit
    locals()
     list 
     h = help '''
import pdb
def seq(n):
    for i in range(n):
        pdb.set_trace() #
        print(i)
n=5
seq(n)