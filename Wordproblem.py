def portal_login_check(email, password):
    if type(email) != str:
        return "Error! Invalid Email! Email must be a string!"
    email = email.strip()
    if "@" not in email:
        return "Error! Invalid Email! Email must include '@'"
    if type(password) != str:
        return "Error! Invalid Password! Password must be a string!"
    password = password.strip()
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