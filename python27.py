def mult_divide():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    return "Multiplication of {} and {} = ".format(num1,num2) + str(num1 * num2), "Division of {} and {} = ".format(num1,num2) + str(num1/num2)
mult, divide = mult_divide()
print(mult + " and " + divide)
