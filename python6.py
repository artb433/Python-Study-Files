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