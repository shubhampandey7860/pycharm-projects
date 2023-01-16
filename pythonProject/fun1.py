# function in python defined by def keyword
#
def function1(): # function declaration
    print('this is function 1')  # statements
def function2():
    print('this is function2')
def main():
    print('this is main function')
    function1()
    function2()  # invoking function or calling function
main()


# write a code for performing all arithmetical operation
def operation(n1,n2,opr):
    if opr=='+':
        print(f'sum of {n1} & {n2} is {n1+n2}')
    elif opr=='-':
        print(f'difference of {n1} & {n2} is {n1-n2}')
    elif opr=='*':
        print(f'multiplication of {n1} & {n2} is {n1*n2}')
    elif opr=='/':
        print(f'division of {n1} & {n2} is {n1/n2}')
    else:
        print(f'enter right operator')


def main():
    n1=int(input("enter any number:"))
    n2=int(input("enter any number"))
    opr=input('enter operation:')
    operation(n1,n2,opr) # calling method
main()


