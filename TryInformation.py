print("Welcome User!\n")
print("Practice")

#Try Genshin Characters :>>>
#For Example, Name: HuTao and Element: Pyro
#Try any input:>>> I just want to use Game Characters hehe

names = []
elements = []
num = int(input("Enter number Information that you want to input: "))


for i in range(num):
    name = input("\nName: ")
    element = input("Element: ")

    names.append(name)
    elements.append(element)

print("\nName\t\t\tElement\n")

for i in range(num):
    print((names[i]),"\t\t\t",(elements[i]))

search_name = input("\nEnter name to search: ")

print("Acquiring Data.....")

if search_name in names:
    index = names.index(search_name)
    element = elements[index]
    print("Name: ",(search_name), "\nElement: ",(element))

else:
    print("Name Not Found")