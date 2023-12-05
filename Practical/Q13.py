user_name = input("Enter Name: ")
try:
    for character in user_name:
        if character.isalpha() or character.isspace():
            continue
        else:
            raise Exception("Entered username contains Number or special Character")
    print("Username is valid and contains no number or special character.")
except:
    print("Entered String contains Number or Special Character")
