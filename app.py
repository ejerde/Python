"""
By Eric Jerde
10/14/2023
"""

from donations_pkg.homepage import donate, show_donations, show_homepage
from donations_pkg.user import register, login

database = {"admin" : "password",
            "Eric" : "1234"
}
donations = []
authorized_user = ""

while True:
    show_homepage(authorized_user) #user

    choice = input("Choose an option:") #menu selection
    if choice == "1":
        username = input("\nEnter username:")
        password = input("Enter password:")
        authorized_user = login(database, username,password)
    elif choice == "2":
        username = input("\nEnter username:")
        password = input("Enter password:")
        authorized_user = register(database, username, password)
    elif choice == "3":
        if authorized_user == "":
            print("\nYou are not logged in.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
    elif choice == "4":
        show_donations(donations)
    elif choice == "5":
        print("\nLeaving DonateMe...")
        break
