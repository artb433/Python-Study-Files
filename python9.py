#!/usr/bin/python3
string = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
string = string[38:66] + string[106:112] + string[0:6]
print(string)

for i in range(1, 10):
    if 1 <= 5:
        print("AAAAAHHHHH")

for i in range(1, 11):
    print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))

for i in range(10):
    print(f"i{i+1} = ", i)

for i in range(1, 21):
    if (i % 2) != 0:
        print(f"i({i}) = ", i)
