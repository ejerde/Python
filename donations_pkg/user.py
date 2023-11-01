#user functions
def login(database, username, password):
    if username in database:
        if password == database[username]:
            print("Welcome back" + username)
        return username
    elif username in database and len(username) != len(password):
        print("Password did not match")
        return ""
    else:
        print("Username was not found, please register")
        return ""

def register(database, username, password):
    if username in database: 
        print("Username already registered.")
        return ""
    if len(username) > 10:
        print("Username must be less than 10 characters")
        return ""
    if len(password) <=5:
        print("password must be more than 5 characters")
        return ""
    else:
        print("\nUsername Registered!")
        return username