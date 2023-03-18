customers = []
while True:
    createEntry = input("Enter Customer (Yes/No) : ")
    createEntry = createEntry[0].lower()
    if createEntry == "n":
        break
    elif createEntry == "y":
        cName = input("Enter Customer name: ")
        customers.append(cName)
    else:
        print("Choose between yes or no")
for customer in customers:
    print(customer)
