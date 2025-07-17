names = ["Atrayee", "Nina"]
my_list = []
for name in names:
    my_list.append(len(name))
print("Before:", my_list)

print("After:", [len(name) for name in names])

print ("Print only names with Even number of chracters:", [name for name in names if len(name)% 2 != 0])
