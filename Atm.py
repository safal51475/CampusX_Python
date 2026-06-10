class Atm:
    #constructor 
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
        
    def menu(self):
        user_input = input("""
    Hi, How can I help you?
    1.Press 1 to create pin
    2.Press 2 to change pin 
    3.Press 3 to check balance
    4.Press 4 to deposit
    5.Press 5 to withdraw                                      
    """)
  
        if user_input =='1':
            #create pin 
            self.create_pin()
        elif user_input =='2':
            #change pin
            self.change_pin()
        elif user_input =='3':
            #check Balance 
            self.check_balance()
        elif user_input == '4':
            #Money for deposit
            self.money_deposit()
        else:
            self.with_draw()
    #creating the pin

    def create_pin(self): 
        user_pin = input('Enter your pin')
        if user_pin.isdigit() and len(user_pin) == 4:
            print("pin created successfully:")
        else:
            print("Error! PIN must be exactly 4 numbers.")

        self.pin = user_pin

        user_balance = int(input('Enter Balance:'))
        self.balance = user_balance

        print("pin created successfully:")
        self.menu()
    
    def change_pin(self):
        old_pin = input("Enter your old pin:")

        if old_pin == self.pin:
            #let them to chnage the pin
            new_pin = input("Enter New Pin:")
            self.pin = new_pin
            print("pin changed successfully ")
            self.menu()
        else:
            print("Your pin is incorrect,Try Again")
            self.menu()
    
    #checking Balance 
    def check_balance(self):
        user_pin = input("Enter your pin:")
        if user_pin == self.pin:
            print("---------------")
            print(f"Your Balance is :{self.balance}|")
            print("---------------")
        else:
            print("Pin is incorrect")

        self.menu()
    
    def money_deposit(self):
        user_pin = input("Enter your pin:")
        if user_pin == self.pin:
            add_amt = int(input("Enter the amount you want to deposit:"))
            self.balance  =  (self.balance or 0) + add_amt 
            print(self.balance)
            
        else:
            print("your pin is incorrect",self.menu())

    def with_draw(self):
        user_pin = input("Enter your pin:")
        if user_pin == self.pin:
            amount = int(input("Enter the amount to withdraw:"))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('withdrawal successful:',self.balance)
                self.menu()
            else:
                print("Insufficent Balance")
        else:
            print("With drawal unsucessful !")
            
        self.menu()
            


    
object = Atm()





