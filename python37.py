myDict = {"fName": "Abdul Rahman", "lName": "Tahiru", "mName": "Baaba", "address": "Tawfiq Mosque Street"}

print("My Name :", myDict["fName"], myDict["mName"], myDict["lName"])
myDict["address"] = "Amaru Junction No.2"
print(myDict)
myDict['region'] = 'Ashanti Region'
print(myDict)
print("Is there an address: ", "address" in myDict)
print(myDict.values())
print(myDict.keys())
for k, v in myDict.items():
    print("Your", k, "is", v)

print(myDict.get("oName", "Not available"))

for i, j in myDict.items():
    print(j)
print(myDict)

engineers = []
fName= input("Enter engineer's first Name: ")
lName = input("Enter engineer's last Name: ")
mName = input("Enter engineer's middle name: ")
engineers.append({"lName": lName, "fName": fName, "mName": mName})
print(engineers)
