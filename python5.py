age = eval(input("Enter age: "))
if (age >= 1) and (age <= 18):
    print("{} is Important".format(age))
elif (age == 21) or (age == 50) or (age > 65):
    print("{} is also Important".format(age))
else:
    print("{} is not important".format(age))
