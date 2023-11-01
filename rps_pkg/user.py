"""
Python Fundamentals
Portfolio project
By Eric Jerde
rev 1.2
10/23/2023
"""

def register(database, username, password):
    if username in database: 
        print("Username already registered.")
        return ""
    if len(username) > 10:
        print("Username must be less than 10 characters")
        return ""
    if len(password) <=2:
        print("password must be more than 2 characters")
        return ""
    else:
        print("\nUsername Registered!")
        return username
"""function for player registration"""