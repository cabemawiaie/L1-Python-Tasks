names = ["Evi", "Madeleine", "Daisy", "Kathy", "Cat", "Hayley"]
names.sort()
print(names)

check_name = input("What name would you like to check in the list: ").strip().title()
if check_name in names:
    print("{}, is already in the list".format(check_name))
else:
    print("{}, is not in the list".format(check_name))


replace_name = input("What name would you like to replace: ").strip().title()
new_name = input("What name would you like to replace it with: ")

print(names.index(replace_name))









