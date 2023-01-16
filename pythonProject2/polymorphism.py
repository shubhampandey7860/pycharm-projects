class Amitabh:
    def acting(self):
        print(f'good in acting')


class Abhishek(Amitabh):
    def acting(self):              # overriding
        print(f'bad in acting')
obj1=Abhishek()
obj1.acting()



#
class Employee:
    def __init__(self):
        self.__empno=None
        self.__ename=None
    def read(self):
        self.__ename=input('enter name:')
        self.__empno=input('enter employee no:')
    def print_data(self):
        print(f'''employee name:{self.__ename}
        employee no:{self.__empno}''')

#
class salariedemployee(Employee):
    def __init__(self):
        super().__init__()
        self.__salary=None
    def read(self):
        super().read()
        self.__salary=float(input('enter salary:'))
    def print_data(self):
        super().print_data()
        print(f'salary:{self.__salary}')


obj1=salariedemployee()
obj1.read()
obj1.print_data()
