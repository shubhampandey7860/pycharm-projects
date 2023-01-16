# oops 1
# object level method
# getattr(object, name, default_value)
#   __getattribute__(object,name,default) // this is object level method
class Employee:
    ename='shubham'
    salary=10000
    empno=101
    @property   # @property enables accessing an object’s method like an attribute:
    def salary(self):
        print(f'{Employee.salary}')
e=Employee
e.salary
print(getattr(e,'ename'))
# setattr method
# setattr(object,name,value)
print(f'name before modification:{e.ename}')
setattr(e,'ename','Yash')
print(f'name after modification:{e.ename}')
