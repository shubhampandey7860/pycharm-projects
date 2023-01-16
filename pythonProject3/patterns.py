# # square
# n=int(input('enter number:'))
# for i in range(n):
#     for j in range(n):
#         print('*',end=' ')
#     print()

#
n=int(input('enter number:'))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

# o/p:
# enter number:9
#  * * * * * * * * *
#  * *           * *
#  *   *       *   *
#  *     *   *     *
#  *       *       *
#  *     *   *     *
#  *   *       *   *
#  * *           * *
#  * * * * * * * * *

#
n=int(input('enter number:'))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
# o/p :
# enter number:9
#  * * * * * * * * *
#  *               *
#  *               *
#  *               *
#  *               *
#  *               *
#  *               *
#  *               *
#  * * * * * * * * *

#
sp=1
n=int(input('enter number:'))
for i in range(n):
    for j in range(sp):
        print('*',end=' ')
    print()
    sp=sp+1
# o/p:
# enter number:7
#  *
#  * *
#  * * *
#  * * * *
#  * * * * *
#  * * * * * *
#  * * * * * * *


