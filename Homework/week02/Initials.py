fullName = input("Please enter your first, middle and last name, separated by a space: "  )
name = fullName.split(" ")
for i in range(len(name)):
    name[i] = name[i][0:1]

name = ". ".join(name)
print(name.upper())