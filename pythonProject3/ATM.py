class Atm:
    def __init__(self):
        self.pin =None
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input(""" Hello how would you like to proceed !
                      1.Enter 1 to create pin
                      2.Enter 2 to deposit
                      3.Enter 3 to withdraw
                      4.Enter 4 check Balance
                      5.Enter 5 to exit 
                      """)
        if user_input == '1':
            self.createPin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.checkBalance()
        elif user_input == '5':
            print('exit()')
        else:
            print('Bye')

    def createPin(self):
        self.pin = input('enter pin:')
        print('pin created successfuly')

    def deposit(self):
        temp = input('enter your pin')
        if temp == self.pin:
            amount = int(input('enter amount:'))
            self.balance = self.balance + amount
            print('deposit successfully')

    def withdraw(self):
        temp = input('enter your pin')
        if temp == self.pin:
            amount = int(input('enter amount:'))
            if amount < self.balance:
                self.balance = self.balance - amount
                print('operation successful')
            else:
                print('insufficient balance')
        else:
            print('invalid pin')

    def checkBalance(self):
        temp = input('enter your pin')
        if temp == self.pin:
            print(f'balance:{self.balance}')
        else:
            print('invalid pin')


# create object of Atm class
sbi = Atm()
sbi.deposit()
sbi.checkBalance()






