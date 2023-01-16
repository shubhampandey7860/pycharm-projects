x = int(input('enter number:'))
y = int(input('enter number:'))
z = int(input('enter number:'))
def minimum(a, b, c):
    if a < b:
        if a < c:
            print(f'{a} is minimum')
        else:
            print(f'{c} is minimum')
    elif b < c:
        print(f'{b} is minimum')
    else:
        print(f'{c} is minimum')


def main():
    minimum(x, y, z)


main()
