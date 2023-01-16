# inheritance with constructor
class A:
    def __init__(self):
        print('init  method in A ')
    def feature1(self):
        print(f'this is feature 1 of class A')
    def feature2(self):
        print(f'this feature 2 of class A')
class B(A):
    def __init__(self):
        print(f'init method in B')
        super().__init__()
    def feature1(self):
        super().feature1()
        print(f'this is feature 1 of class B')
    def feature2(self):
        super().feature2()
        print(f'this is feature 2 of class B')

obj1=B()
obj1.feature1()
obj1.feature2()