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
    digit_found = False
    for char in password:
        if char.isdigit():
            digit_found = True
            break
    if not digit_found:
        return "Error! Invalid Password! Password must include at least one digit!"
    upper_found = False
    for char in password:
        if char.isupper():
            upper_found = True
            break
    if not upper_found:
        return "Error! Invalid Password! Password must include at least one uppercase letter!"
    return {
        "email": email,
        "password": password
    }
print(portal_login_check("testemail123@gmail.com", "Nopass18"))