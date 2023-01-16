# multiple  inheritance
class A:
    def feature1(self):
        print(f'this is feature 1')

    def feature2(self):
        print(f'this is feature 2')


class B():
    def feature3(self):
        print(f'this is feature 3')

    def feature4(self):
        print(f'this is feature 4')


class C(A,B):
    def feature5(self):
        print(f'this is feature 5')

    def feature6(self):
        print(f'this is feature 6 ')
obj1=C()
obj1.feature1()
obj1.feature2()
obj1.feature3()
obj1.feature4()
obj1.feature5()
obj1.feature6()
