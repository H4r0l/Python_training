password = input('Insert your password: \n ')

special_characters = "!@#$%^&*()"

def password_checker(password):
    for char in special_characters:
        if char in password == False:
            print('Your password does not contain special characters')
            return False
    if(len(password) < 8):
        print('Your password is too short')
        return False
    if any(char.isdigit() for char in password) == False:
        print('Your password does not contain numbers')
        return False
    if any(char.isupper() for char in password) == False:
        print('Your password does not contain uppercase letters')
        return False
    return True

if password_checker(password) == True:
    print('Your password is good to go')
