# Random module for genrating random numbers
import random
# randrange method gives random number in given range
c=random.randrange(10,30) # it generates random number between 10 to 30
a=random.randrange(1,100,2) # its gives only odd digits
b=random.randrange(2,100,2)
print(a)
print(b) # it only gives even number
print(c)


# choice() method return a random element from sequence or iterable
a=['Apple','Banana','Orange','Mango']
print(random.choice(a))

#  The random() method returns a random floating number between 0 and 1.
a=random.random()
print(a)

#



