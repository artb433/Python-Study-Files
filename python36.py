customers = []
while True:
    createEntry = input("Enter Customer (Yes/No) : ")
    createEntry = createEntry[0].lower()
    if createEntry == "n":
        break
    elif createEntry == "y":
        fName = input("Enter Customer first name: ")
        lName = input("Enter Customer last name: ")
        customers.append({"first Name": fName, "last Name": lName})
    else:
        print("Choose between yes or no")
for customer in customers:
    print(customer['last Name'], customer['first Name'])

