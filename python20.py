for i in range(0, 10):
    for j in range(0, 10):
        if j > i:  # check if j is greater than i before printing
            if i == 8 and j == 9:
                print("{}{}".format(i, j))
                break
            print("{}{}".format(i, j), end=", ")
