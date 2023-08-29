def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        return result


numFibValues = int(input("How many fibonacci values should be found: "))
i = 1
while i < numFibValues:
    fibValue = fib(i)
    print(fibValue)

    i += 1

print(f"Here is fibonacci values of {numFibValues} numbers")