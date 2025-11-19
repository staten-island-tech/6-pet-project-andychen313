""" def portal_login(email, password):
    email_check = False
    password_check = False
    while email_check == False:
        for e in email:
            if e == "@":
                email = True
            else:
                print("Invalid Email! Make sure it is a valid email and includes '@'")
    while password_check == False:
        for p in password:
            if len(password) >= 8:
                password = True
            else:
                print("Invalid Password! Password must contain at least 8 characters!")
portal_login("emailtest123@gmail.com", "Lkf001@") """

""" def portal_login_check(email, password):
    email.strip(" ")
    if "@" not in email:
        print("Error! Invalid Email! Email must include @")
    else:
        print("Valid Emal!")
    password.strip(" ")
    if len(password)
portal_login_check("emailtest123gmail.com") """
    
""" def portal_login_check(password):
    password.strip(" ")
    if len(password) <= 8:
        print("Error! Invalid Password! Password must include at least 8 characters!")
    elif 
    else:
        print("Valid Email!") """

def portal_login_check(email, password):
    if type(email) != str:
        return "Error! Invalid Email! Email must be a string!"
    if "@" not in email:
        return "Error! Invalid Email! Email must include '@'"
    if type(password) != str:
        return "Error! Invalid Password! Password must be a string!"
    if len(password) < 8:
        return "Error! Invalid Password! Password must include at least 8 characters!"
    found_digit = False
    for char in password:
        if char.isdigit():
            found_digit = True
            break
    if not found_digit:
        return "Error! Invalid Password! Password must include at least one digit!"
    found_upper = False
    for char in password:
        if char.isupper():
            found_upper = True
            break
    if not found_upper:
        return "Error! Invalid Password! Password must include at least one uppercase letter!"
    return {
        "email": email,
        "password": password
    }
print(portal_login_check("emailtest123@gmail.com", "BestPass123"))