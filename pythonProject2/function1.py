# findinding maximum value
def max(x,y,z):
    if x>y:
        if x>z:
            print(f'{x} is max')
        else:
            print(f'{z} is max')
    elif y>z:
        print(f'{y} is max')
    else:
        print(f'{z} is max')
def main():
    x=int(input('enter value of x:'))
    y=int(input('enter value of y:'))
    z=int(input('enter value of z:'))
    max(x,y,z)
main()

