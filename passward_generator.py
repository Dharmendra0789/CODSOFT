#program to build a password generator of desired length
import random
import pyperclip
#checking  he password can be built or not
print("Choose among the following that you want:\n1. A random password.\n2. A password of your combinations.")
option = int(input("1 or 2 "))
if option == 1:
    length = int(input("Enter the required length of the password"))
    if length <1:
        print("Length is too small")
    else:
        print("YOUR PASSWORD IS :",end='\n')
        for i in range(length):
            print(chr(random.randint(32,127)),end='')
elif option == 2:
    password = []
    alpha = int(input("Enter the number of alphabets you want."))
    digits = int(input("Enter the number of digits you want."))
    special = int(input("Enter the number of special characters you want."))
    print("Your Password is : ",end = ' ')
    for i in range(alpha):
        password.append(random.randrange(65,123))
    for i in range(digits):
        password.append(random.randrange(48,58))
    for i in range(special):
        password.append(random.randrange(32,47))
    random.shuffle(password)
    for j in password:
        print(chr(j),end='')
     
        
        