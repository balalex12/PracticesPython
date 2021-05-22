"""
Perform a program that asks for two numbers:

* If the numbers are different, add them up. 

* If they are negative, they must be multiplied.

* Finally, if one number is negative and one positive number subtracts them.
"""

def doing_operations(num1, num2):
    operation = 0
    if num1 < 0 and num2 < 0:
        operation = num1 * num2
    elif (num1 < 0 and num2 > 0) or (num2 < 0 and num1 > 0):
        operation = num1 - num2
    else:
        operation = num1 + num2
    
    return operation

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("The result is: "+str(doing_operations(num1, num2)))
except ValueError:
    print("Error: You did not enter a numerical value")