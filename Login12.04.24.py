#  User input for name
#  User input for password
 
#  create username & password if no account
 
#  store the details
 
#  check the details
 
#  if valid then accept & enter program
 
#  if invalid then decline
 
import json
import getpass

filename = "logins.json"

def login(file):
    global logins
    logins = ""
    with open(file) as filename:
        logins = "logins.json".load(filename)
    return logins
    
# print(login(filename))

def validate(username, password):
    if logins[username] == password:
        print("welcome")
    else:
        print("bye bye bot")
        
def create_user(username, password):
    logins[username] = password
    output = json.dumps(logins, indent=4)
    with open(filename, "w") as file:
        file.write(output)
        
##############

username = input("What is your username? ")
password = input("What is your password? ")

choice = input("Do you need to set up a new account? Y/ N \n ").lower()

if choice == "y":
    login(filename)
    create_user(username, password)
    validate(username, password)

elif  choice == "n":
    print("Welcome")
    login(filename)
    validate(username, password)