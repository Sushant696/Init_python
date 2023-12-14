# validate the emailaddress and password lenthh
# check for the presence of special characters in the password
# ensure that both username and password are not empty

password = input('Enter your password:')
emailaddress = input('Enter you emailaddress: ')
len = len(password)


# password validation
def passwordFunc(password, len):
    if (len >= 8):
        if ('#' in password or "*" in password):
            global validPassword
            validPassword = 1
            print(validPassword, 'hello')
            print("You password is valid and saved")
        else:
            print('please enter a valid password which contains a special character and have more than 8 characters')
    else:
        print("please enter a password that is more than 8 characters long")


passwordFunc(password, len)

# Email validation
print(validPassword, 'hello')


def emailFunc(emailaddress):
    if (emailaddress != " "):
        if (emailaddress.endswith("@gmail.com") and validPassword):
            # return emailaddress
            print("Your password and email both are valid and saved")
        else:
            print('please enter a valid emailaddress with proper format')
    else:
        print("Email address cannot be empty")


emailFunc(emailaddress)
