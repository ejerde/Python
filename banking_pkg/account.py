#function to show balance of account
def show_balance(balance):
    print(f"The current balance is $", float(balance))
#function to deposit to account    
def deposit(balance):
    amount = input("Enter amount to deposit:")
    return int(balance) - int(amount)
#function to withdraw from account
def withdraw(balance):
    withdraw_amount = input("Enter amount to withdraw:")
    return int(balance) - int(withdraw_amount), print("Updated balance: $", int(balance) - int(withdraw_amount))
#function to logout    
def logout(name):
    print(f"Goodbye {name}")
