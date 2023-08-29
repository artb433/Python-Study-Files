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


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        return result


print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))

