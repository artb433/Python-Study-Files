num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
total_sum = num1 + num2
difference = num1 - num2
product = num1*num2
quotient = num1/num2
remainder = num1 % num2
print("{} + {} = {}".format(num1, num2, total_sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} / {} = {:.2f}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
print("{} * {} = {}".format(num1, num2, product))
