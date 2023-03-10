# Ask the user to input their name

# name = input("What is your name: ")
# print('Hello ', name)


# num1 = int(input('Enter first number '))
# num2 = int(input('Enter second number '))
# total_sum = num1 + num2
# difference = num1 - num2
# product = num1*num2
# quotient = num1/num2
# remainder = num1%num2
# print("{} + {} = {}".format(num1, num2, total_sum))
# print("{} - {} = {}".format(num1, num2, difference))
# print("{} / {} = {}".format(num1, num2, quotient))
# print("{} % {} = {}".format(num1, num2, remainder))
# print("{} * {} = {}".format(num1, num2, product))


# miles = int(input('Enter distance in miles '))
# miles_to_kilometers = miles * 1.60934
# print("{} miles equals {}".format(miles,miles_to_kilometers))


# num1, operator, num2 = input('Enter Calcutation: ').split()
# num1 = int(num1)
# num2 = int(num2)
# if operator == '+':
#     print('{} {} {} is {}'.format(num1, operator, num2, num1+num2))
# if operator == '-':
#     print('{} {} {} is {}'.format(num1, operator, num2, num1-num2))
# if operator == '*':
#     print('{} {} {} is {}'.format(num1, operator, num2, num1*num2))
# if operator == '/':
#     print('{} {} {} is {}'.format(num1, operator, num2, num1/num2))
# else:
#     print("Use either + , - , / , *")


# age = eval(input("Enter age: "))
# if (age >= 1) and (age <= 18):
#     print("{} is Important".format(age))
# elif (age == 21) or (age == 50) or (age > 65):
#     print("{} is also Important".format(age))
# else:
#     print("{} is not important".format(age))


age = eval(input("Enter age: "))
if age < 5:
    print("Too young for school")
elif age == 5:
    print('Go to kindergarten')
elif (age >= 6) and (age <= 17):
    grade = age - 5
    print("Goes to grade {}".format(grade))
else:
    print('Goes to college')

