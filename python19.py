for i in range(00, 100):
    if i != 99:
        print("{0:0=2d}".format(i), end=", ")
    else:
        print("{}".format(i))
