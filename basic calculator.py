print("**** Caculator ****")

print("\n")

number1 =  float(input("Enter first number:"))
number2 =  float(input("Enter second number:"))

print("Enter 1 for 'Addition'" )
print("Enter 2 for 'Subtraction'")
print("Enter 3 for 'Multiplication'")
print("Enter 4 for 'Division'")

Enter_Number1 = int(input("Choose the operation you want to perform by entering the corresponding number:"))

if Enter_Number1 == 1:
    print("The result of addition is:", number1 + number2)
elif Enter_Number1 == 2:
    print("The result of subtraction is:", number1 - number2)
elif Enter_Number1 == 3:    
    print("The result of multiplication is:", number1 * number2)
elif Enter_Number1 == 4:
    if number2 != 0:
        print("The result of division is:", number1 / number2)
    else:
        print("Invalid input")
