usernames = {
    'Adriana': '123456',
    'john':'GVEST',
    'Richard': 'REJ321',
    'Caleb':'875'
    }
username = input("Please Enter Your Username: ")
if username in usernames:
    password= input("Please Enter Your Password: ")
    if usernames[username] == password: #this gets the password value of the user
        
        print("Thank You")
    else : 
        print(" You Have enetered Incorrect Password")
else :
    print ("You are not registered")
