main_string = input("Enter the full phrase: ")
main_string = main_string.split()
for i in main_string:
    acronym = i[0].upper()
    print(acronym, end="")
