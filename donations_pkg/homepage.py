
def show_homepage(username):
    print("")
    print("User:" + username)
    print("          === DonateMe Homepage ===      ")
    print("------------------------------------------")
    print("| 1.  Login     | 2.   Register         |")
    print("------------------------------------------")
    print("| 3.  Donate    | 4.   Show Donations   |")
    print("------------------------------------------")
    print("|               5.  Exit                |")
    print("------------------------------------------")

def donate(username):
    donation_amt = float(input("\nEnter amount to donate: ")) #donation functions

    donation = username + " donated $" + str(donation_amt)
    print("Thank you for donating!")
    return donation
    
def show_donations(donations):
    print("\n--All Donations ---")
    if len(donations) == 0:
        print("There are no donations at this time.")
    else:
        for donation in donations: 
            print(donation)
            