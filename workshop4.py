
"""
Week 4 workshop 
By: Eric Jerde
Date: 10/21/2023
"""

# used to type hint BankUser within Bankuser in Python 3.7+
from __future__ import annotations

class User:

    def __init__(self, name: str, pin: int, password: str):
        self.name = name
        self.pin = pin
        self.password = password
    
    def change_name(self, new_name: str):
            
        self.name = new_name

    def change_pin(self, new_pin: int):
            
        self.pin = new_pin

    def change_password(self, new_pw: str):
            
        self.password = new_pw


class BankUser(User):

    def __init__(self, name: str, pin: int, password: str):
       
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(f"{self.name} has an account balance of: {self.balance}")


    def withdraw(self, amount: int):
        self.balance -= amount

    def deposit(self, amount: int):
        self.balance += amount

    def transfer_money(self, user: BankUser, amount: int):
        print( "You are transferring $" + str(amount), "to", (user.name))
        print("Please enter Pin to continue")

        pin_number = int(input(f"Enter{self.name} Pin:" ))
        if pin_number != self.pin:
            print("Incorrect pin, transfer cancelled")
            
            return False
        
        print("Transfer Authorized")
        print( "You are transferring $" + str(amount), "to", (user.name))
        
        self.withdraw(amount)
        user.deposit(amount)
        
        return True

    def request_money(self, user: BankUser, amount: int):
       
        print("You are requesting $" + str(amount),"from", (user.name))
        print("User pin is required")

        pin_number = int(input(f"Enter{self.name} Pin:" ))
        if pin_number != self.pin:
            print("Incorrect pin, transfer cancelled")
            return False
        
        password = input("Enter your password:")
        if password != self.password:
            print("Incorrect password, transfer cancelled")
            return False

        if pin_number and password:
            print("Transfer request authorized")
            print(user.name + "sent $" + str(amount))

            user.withdraw(amount)
            self.deposit(amount)

            return True
        else:
            return False


# # # Driver Code for Task One
# # # Output: Bob 1234 password

#user1 = BankUser("Bob", 1234, "password")
#print(user1.name, user1.pin, user1.password)

# # # Driver Code for Task Two
# # # Output: Bob 1234 password
# # # Output: Bobby 4321 newpassword

#user1 = BankUser("Bob", 1234, "password")
#print(user1.name, user1.pin, user1.password)
#user1.change_name("Bobby")
#user1.change_pin(4321)
#user1.change_password("newpassword")
#print(user1.name, user1.pin, user1.password)


# # # Driver Code for Task Three
# # # Output: Bob 1234 password 0

#bankuser1 = BankUser("Bob", 1234, "password")
#print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)


# # # Driver Code for Task Four
# # # # Output:
# # #   Alice has an account balance of: 0
# # #   Alice has an account balance of: 1000.0
# # #   Alice has an account balance of: 500.0

#bankuser1 = BankUser("Bob", 1234, "password")
#bankuser1.show_balance()
#bankuser1.deposit(1000.0)
#bankuser1.show_balance()
#bankuser1.withdraw(500.0)
#bankuser1.show_balance()


# # # Driver Code for Task Five
# # # Output:
# # #   Alice has an account balance of: 5000
# # #   Bob has an account balance of: 0

# # #   You are transferring $500 to Bob
# # #   Authentication required
# # #   Enter your PIN: 2345
# # #   Transfer authorized
# # #   Transferring $500 to Bob
# # #   Alice has an account balance of: 4500
# # #   Bob has an account balance of: 500

# # #   You are requesting $250 from Bob
# # #   User authentication is required...
# # #   Enter Bob's PIN: 1234
# # #   Enter your password: password
# # #   Request authorized
# # #   Bob sent $250
# # #   Alice has an account balance of: 4750
# # #   Bob has an account balance of: 250


#bankuser1 = BankUser("Bob", 1234, "password")
#bankuser2 = BankUser("Alice", 2345, "newpassword")
#bankuser2.deposit(5000)
#bankuser2.show_balance()
#bankuser1.show_balance()
#print()

#transferred = bankuser2.transfer_money(bankuser1, 500)
#bankuser2.show_balance()
#bankuser1.show_balance()
#print()

#if transferred:
    #bankuser2.request_money(bankuser1, 250)
    #bankuser2.show_balance()
    #bankuser1.show_balance()
