class Person:
    def __init__(self, name):
        self.name = name

    @property
    def Person_name(self):
        return self.name


P1 = Person('shubham')
p2=P1.Person_name
print(f'name of person is :{p2}')
