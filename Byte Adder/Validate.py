from Conversion import *

def validate_binary(n):
    if n == "":
        return[True, "No number entered. Please make sure to enter a number."]
    try:
        checkNumber = int(n)
    except:
        return[True, "Special characters are not acceptable."]
    if len(n) > 8:
        return[True, "Please make sure the number you have entered lies between 00000000 and 11111111."]
    if int(n) < 0:
        return[True, "Please enter a positive number"]
    if set(n) == {'0'} or set(n) == {'0','1'} or set(n) == {'1'}:
        return[False]
    else:
        return [True, "Invalid input for binary number. Please enter 0 and 1."]
    return[False]
    
def validate_decimal(n):
    if n == "":
        return[True, "No number entered. Please make sure to enter a number."]
    try:
        checkNumber = int(n)
    except:
        return[True, "Special characters are not acceptable."]
    if int(n) < 0:
        return[True, "Please enter a positive number"]
    if int(n) > 255:
        return[True, "Please make sure the number you have entered lies between 0 and 1."]
    return[False]

def check_Length(n):
    while len(n) != 8:
        n = '0' + n

