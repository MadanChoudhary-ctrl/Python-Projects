from Validate import *
from Conversion import *
from Byte_adder import *

def main():
    c = 'y'
    while c == 'y' or c == 'Y':
        print("Select any: \n1. Binary Addition  \n2. Decimal Addition")
        s = int(input("Enter 1 for Binary Addition and 2 for Decimal Addition: "))
        if s == 1:
            print("You have selected Binary Addition .")
            num1 = input("Enter first binary number: ")
            flag = False
            while(not flag):
                if validate_binary(num1)[0]:
                    print("Error...",validate_binary(num1)[1])
                    num1 = input("Enter first binary number: ")
                else:
                    check_Length(num1)
                    flag = True
                    break
            num2 = input("Enter second binary number: ")
            flag = False
            while(not flag):
                if validate_binary(num2)[0]:
                    print("Error...",validate_binary(num2)[1])
                    num2 = input("Enter second binary number: ")
                else:
                    check_Length(num2)
                    flag = True
                    break
            flag_sum = False
            while(not flag_sum):
                if int(binaryToDecimal(num1)) + int(binaryToDecimal(num2)) > 255:
                    print("Error... Please make sure the sum is not more than 11111111.")
                    num1 = input("Enter first binary number: ")
                    flag = False
                    while(not flag):
                        if validate_binary(num1)[0]:
                            print("Error...",validate_binary(num1)[1])
                            num1 = input("Enter first binary number: ")
                        else:
                            check_Length(num1)
                            flag = True
                            break
                    num2 = input("Enter second binary number: ")
                    flag = False
                    while(not flag):
                        if validate_binary(num2)[0]:
                            print("Error...",validate_binary(num2)[1])
                            num2 = input("Enter second binary number: ")
                        else:
                            check_Length(num2)
                            flag = True
                            break
                else:
                    print("_________________Binary Addition Result___________\n")
                    print("First Number           Second Number           Sum\n")
                    print(f"{decimalToBinary(binaryToDecimal(num1))}                {decimalToBinary(binaryToDecimal(num2))}            {adder(num1,num2)}\n")
                    print(f"{binaryToDecimal(num1)}                          {binaryToDecimal(num2)}                  {binaryToDecimal(adder(num1,num2))}\n__________________________________________________")
                    flag_sum = True
                    break

        elif s == 2:
            print("Decimal Addition is selected.")
            num1 = input("Enter first decimal number: ")
            flag = False
            while(not flag):
                if validate_decimal(num1)[0]:
                    print("Error...",validate_binary(num1)[1])
                    num1 = input("Enter first decimal number: ")
                else:
                    a = int(num1)
                    num1 = decimalToBinary(num1)
                    flag = True
                    break
            num2 = input("Enter second decimal number: ")
            flag = False
            while(not flag):
                if validate_decimal(num2)[0]:
                    print("Error...",validate_decimal(num2)[1])
                    num2 = input("Enter second decimal number: ")
                else:
                    b = int(num2)
                    num2 = decimalToBinary(num2)
                    flag = True
                    break
            flag_sum = False
            while(not flag_sum):
                sum = a + b
                if sum > 255:
                    print("Error... Please make sure the sum is not more than 255.")
                    num1 = input("Enter first binary number: ")
                    flag = False
                    while(not flag):
                        if validate_decimal(num1)[0]:
                            print("Error...",validate_decimal(num1)[1])
                            num1 = input("Enter first decimal number: ")
                        else:
                            a = int(num1)
                            num1 = decimalToBinary(num1)
                            flag = True
                            break
                    num2 = input("Enter second decimal number: ")
                    flag = False
                    while(not flag):
                        if validate_decimal(num2)[0]:
                            print("Error...",validate_decimal(num2)[1])
                            num2 = input("Enter second decimal number: ")
                        else:
                            b = int(num2)
                            num2 = decimalToBinary(num2)
                            flag = True
                            break
                else:
                    print("______________Decimal Addition Result_____________\n")
                    print("First Number           Second Number           Sum\n")
                    print(f"{num1}                {num2}            {adder(num1,num2)}\n")
                    print(f"{binaryToDecimal(num1)}                          {binaryToDecimal(num2)}                  {binaryToDecimal(adder(num1,num2))}\n__________________________________________________")
                    flag_sum = True
                    break
        else:
            print("Please make sure you have selected a valid option.")
        c = input("Continue or Quit?(Type 'y' to continue and 'n' to quit): ")
    print("Thank you for using the Byte Adder.")
main()
        
    
        
            
    
                                
        
        
        
