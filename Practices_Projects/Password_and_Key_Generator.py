#AUTHOR = BY BALALEX12
"""
This is a script to generate a random password or keys, deoending
on how the user needs it.

"""

import random
import string
import os 
import subprocess

#This method is responsible for cleaning the terminal 
def terminal_cleaning():
    try:
        os.system('cls')
    except:
        os.system('clear')

#This method will generate the keys or passwords that the user wants.
def generator():
    who = subprocess.getoutput("whoami")
    
    

    terminal_cleaning() 
    generated = []
    result = ""
    replace = who.replace("\\"," ")
    user = replace.split()[-1]
    print("*** Hi "+user+", welcome to the password generator! ***\n\n")
    op = input("What do you want to generate? \na) Password\nb) Numeric Key\nEnter: ")
    
    if len(op) == 1:
        terminal_cleaning()        
        amount_digits = int(input("How many digits do you want?\nEnter: "))

        terminal_cleaning()
        amount_get = int(input("How many do you wan to get?\nEnter: "))

        if op == 'a':
            #This line joins the characters and digits that are imported from the string package to form a 
            #password by mixing alphanumeric, lowercase and uppercase.
            characters = string.ascii_letters + string.digits 

            for i in range(amount_get): #It will iterate over the number of passwords requested by the user.
            
                #The result will join the random character in a single line based on the iteration of the number of digits requested.
                result = ''.join([random.choice(characters) for a in range(amount_digits)])
                generated.append(result) #Add each password to the list.

            print("\nGenerating your password...")
            input("Press Enter...")
            terminal_cleaning()
            print("Password Generated: \n")

            for x in generated: #It will print each password
                print(x)                

        #In the next phase or option it does the same logic as the previous one except that it will only form numbers such as keys or PINs.
        elif op == 'b':
            characters =string.digits

            for i in range(amount_get):
                result = ''.join([random.choice(characters) for a in range(amount_digits)])
                generated.append(result)

            print("\nGenerating your password...")
            input("Press Enter...")
            terminal_cleaning()
            print("Key Generated: \n")

            for x in generated:
                print(x)        
        
        else:
            print("Error: Invalid entered value") #It will throw an error in case a non-existent option has been entered.        

    else:
        print("Error: Invalid entered value") #It will throw an error in case a string with more than one digit has been entered.
    


generator()


#QVVUSE9SOiBCWSBCQUxBTEVYMTI=