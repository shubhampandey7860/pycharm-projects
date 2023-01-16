n=int(input('enter number:'))
char=input('enter charcter:')
t=''
for i in char:
     if i>='a' and i<='z':
         st=ord(i)-97
         res=st+n
         rem=res%26
         out=97+rem
         result=chr(out)
         t+=result
     elif i>='A'and i<='Z':
         st = ord(i) - 65
         res = st + n
         rem = res % 26
         out = 65 + rem
         result = chr(out)
         t += result

print(f'{char}:{t}')

# Emrip number
n=int(input('enter number:'))
num=n
t=0
while n!=0:
    rem=n%10
    n//=10
    t=t*10+rem
if t==num:
    print(f'not a Emrip number:')
else:
    if num>1:
        for i in range(2,num//2+1):
            if num%i==0:
                print(f'not a emrip number')
                break
        else:
            if t>1:
                for i in range(2,t//2+1):
                    if t%i==0:
                        print('not a emrip number')
                        break
                else:
                    print(f'given number is emrip')
            else:
                print(f'not a emrip number')
    else:
        print(f'not a emrip number')



# count
a=int(input('enter number:'))
c=0
while a!=0:
    a//=10
    c+=1
print(f'count of  digit is :{c}')

# emrip number
n=int(input('enter number: '))
num=n
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n//=10
if rev!=num:
    for a in range(2,num//2+1):
        if num%a==0:
            print(f'not emrip number')
            break
    else:
        for b in range(2,rev//2+1):
            if rev%b==0:
                print(f'not a emrip number')
                break
        else:
            print('emrip number')

else:
    print(f'not a emrip number')


# niven number
n=int(input('enter number:'))
num=n
t=0
while n!=0:
    rem=n%10
    t+=rem
    n//=10
if num%t==0:
    print(f'number is niven ')
else:
    print(f' number is not niven')

# palyPrime
n=int(input('enter number: '))
num=n
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n//=10
if num==rev:
    for i in range(2,num//2+1):
        print('Not palyPrime')
        break
    else:
        print(f'palyprime')
else:
    print('not palyPrime')

