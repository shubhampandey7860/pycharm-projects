class Employee:
    def __init__(self):
        self.__empno=None
        self.__ename=None
    def set_data(self):
        self.__empno=int(input('enter employee no:'))
        self.__ename=input('enter name:')
    def print_data(self):
        print(f'employee name:{self.__ename}')
        print(f'employee no:{self.__empno}')
class salary(Employee):
    def __init__(self):
        super().__init__()
        self.__salary=None
    def set_data(self):
        super().set_data()
        self.__salary=input('enter employee salary:')
    def print_data(self):
        super().print_data()
        print(f'employee salary:{self.__salary}')

obj1=salary()
obj1.set_data()
obj1.print_data()
