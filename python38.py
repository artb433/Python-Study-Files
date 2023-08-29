customers = []


def createentry():
    entry = input("Create entry (yes/no): ")
    return entry
if createentry() == 'n':
    print(customers)
elif createentry() == 'y':
    customerName = input("Enter customer name: ")
    customers.append(customerName)


def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result


print(factorial(13))
