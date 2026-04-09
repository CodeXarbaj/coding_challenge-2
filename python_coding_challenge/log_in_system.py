# username and password
user_id = "admin"
password_ = "1234"

# Take input
user = input("Enter username: ")
password = input("Enter password: ")

# Validate login
if user == user_id and password == password_:
    print("Login Successful")
else:
    print("Invalid Credentials")