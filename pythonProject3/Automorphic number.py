# Python program to check if a number is Automorphic
# Function to check Automorphic number
def isAutomorphic(N):
    # Store the square
    sq = N * N
     # Start Comparing digits
    while (N > 0):
        # Return false, if any digit of N doesn't
       # match with its square's digits from last
       if (N % 10 != sq % 10):
            return False
       N //= 10
       sq //= 10

    return True


# Driver code
N = int(input('enter number:'))
if isAutomorphic(N):
    print("Automorphic")
else:
     print("Not Automorphic")


N=int(input('enter string:'))
sq=N*N
while N>0:
    if N%10!=sq%10:
        print('Not Automorphic Number')
    N //= 10
    sq //= 10

print('Automorphic Number')

num = int(input("Enter a number you want to check: \n"))

# # # calculating the number of digits
num_of_digits = len(str(num))

 # computing the square of a number
square = num ** 2

# obtaining the last digits
last_digits = square % pow(10, num_of_digits)

# # # comparing the digits of number with input
if last_digits == num:
     print("Yes, {} is an automorphic number".format(num))
else:
     print("No, {} is not an automorphic number".format(num))

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a)):
        if i==0 :
             a[i][j]=3-j

print(a)
# #

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(a)):
    for j in range(len(a)):
         if i==0 and j==0:
             a[i][j]=a[i][len(a)-1]

print(a)
# #

s='ENGINEERING'
d={}
for i in s:
     if i not in d:
         d[i]=1
     else:
         d[i]+=1
for k,v in d.items():
     print(f'{k}:{v}')

# # # highest value in dict
h=list(d.values())
print(h)
res=h[0]
# # # finding key of given key
for i in range(1,len(h)):
     if res<h[i]:
         res=h[i]
print(res)
# #

for k,v in d.items():
     if v==res:
         print(f'{k}')



# # # wap to most frequetly world in string
s='we dont practice but we want job'
l=s.split()
d={}
for i in l:
     if i not in d:
        d[i]=1
     else:
         d[i]+=1
for k,v in d.items():
     print(f'{k}:{v}')


s='we dont practice but we want job'
l=s.split()
d={}
for i in l:
    if i not in l:
         d[i]=1
    else:
         d[i]+=1
vl=list(d.values())
H=vl[0]
for i in range(1,len(vl)):
     if H<vl[i]:
         H=vl[i]
print(H)

for k,v in d.items():
    if H==v:
        print(k)

#  wap to print lenthiest world in given string
s='we dont practice but we want job'
d={}
l=s.split()

#
for i in l:
    if i not in d:
        d[i]=len(i)
print(d)
lst=list(d.values())
h=lst[0]
for i in range(1,len(lst)):
    if h<lst[i]:
         h=lst[i]
print(h)
for k,v in d.items():
     if h==v:
         print(f'{k}')


for k,v in d:
     if h==v:
         print(f'{k}:{v}')
