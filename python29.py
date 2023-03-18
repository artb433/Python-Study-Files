def sumAll(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print("Sum :",sumAll(1,2,4,5,3,5,6,43,5,6,4,6,4,3,5,6,4,3,5,6,6,))
