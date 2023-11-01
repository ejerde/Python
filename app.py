from banking_pkg import account
#customer atm selection menu
def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
#Customer Registration 
print("          === Automated Teller Machine ===          ")
name = input("Enter name to register:")
pin = input("Enter PIN:")
balance = 0
print(name, "has been registered with a starting balance of $" + str(balance))
#Customer Login while loop
print("LOGIN")
while True:
    name_to_validate = input("Enter Name:")
    pin_to_validate = input("Enter Pin:")
    if name_to_validate == name and pin_to_validate == pin: 
        print("Login Successful")
        break
    else:
        print("Invalid Credentials!")
        continue
#ATM menu while loop
while True:
    (atm_menu(name))
    option = input("Choose an Option:")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        account.deposit(balance)
    elif option == "3":
        account.withdraw(balance)
    elif option == "4":
        account.logout(name)
