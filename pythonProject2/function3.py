# function with argument
def area(l, b):
    a = l * b
    print(f'area of circle: {a}')


def main():
    l = float(input('enter length:'))
    b = float(input('enter width:'))
    area(l, b)


main()
