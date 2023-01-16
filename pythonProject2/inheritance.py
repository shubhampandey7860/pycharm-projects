#  inheritance
# single level inheritance
class A:
    def feature1(self):
        print(f'feature 1 is working')
    def feature2(self):
        print('feature 2 is working')
class B(A):
    def feature3(self):
        print(f'feature 3 is working')
    def feature4(self):
        print(f'feature 4 is working ')
obj1=B()
obj1.feature1()
obj1.feature2()
obj1.feature3()
obj1.feature4()