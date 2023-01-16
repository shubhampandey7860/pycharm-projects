# write a program to check wheter a number is prime or not
def prime(num):
    i=1
    c=0
    while num>=i: # 1,2,3,4,5
        if num%i==0:
            c+=1
        i+=1
    if c==2:
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')
def main():
    num=int(input('enter any number:'))
    prime(num)
main()




# write a program to print given number is pal or not
def pal(num):
    n=num
    sum=0
    while num>0:
        r=num%10
        sum=sum*10+r
        num=num//10
    print(f'sum of number {sum}')
    if n==sum:
        print(f'{n} is pal')
    else:
        print(f'{n} is not pal')
def main():
    num=int(input("enter any number"))
    pal(num)
main()


# write a program to calculate given number is armstrong or not
num=input('enter any number')
b=len(num)
a=int(num)
c=a
sum=0
while a>0:
    r=a%10
    sum=sum+r**b
    a=a//10
print(f'{sum}')
if  sum==c:
    print(f'num is arm')
else:
    print(f'number is not arm')
#    prime number

num=int(input('enter any number:'))
c=0
i=1
while num>=i:
    if num%i==0:

        c+=1
    i+=1
if c==2:
    print(f'prime')
else:
    print('Non-prime')









