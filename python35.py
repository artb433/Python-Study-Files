mydict = {"fname": "Abdul Rahman", "lname": "Tahiru", "job": "Software Engineer"}
mydict["city"] = "Washington"
print("My first name is {} and I'm a {} living in {}".format(mydict["fname"], mydict["job"], mydict["city"]))
print("Is there country in:", "country" in mydict)

for k, v in mydict.items():
    print(k, v)
print(mydict.get("hobby", "not recorded"))
del mydict["lname"]
print(mydict)

employees = []
fname = input("Enter employee fist name: ")
lname = input("Enter employee last name: ")
employees.append({'fname': fname, 'lname':lname})
print(employees)
