# multi level inheritance
class A:
    def Feature1(self):
        print(f'this is feature 1')

    def Feature2(self):
        print(f'this is feature 2')


class B(A):
    def Feature3(self):
        print(f'this is feature 3')

    def Feature4(self):
        print(f'this is feature 4')


class C(B):
    def Feature5(self):
        print(f'this is feature 5')

    def Feature6(self):
        print(f'this is feature  6 ')


obj1 = C()

obj1.Feature1()
obj1.Feature2()
obj1.Feature3()
obj1.Feature4()
obj1.Feature5()
obj1.Feature6()