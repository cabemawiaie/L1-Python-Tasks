names = ("Evi", "Madeleine", "Dan", "Kelsey", "Cayden", "Hayley")
sorted_names = sorted(names)
for names in sorted_names:
    print(names)

username = input("What name would you like to see in the list: ").strip().title()

if username in names:
    print("{} is already in the list".format(username))
else:
    print("{} can not be found in the list".format(username))
