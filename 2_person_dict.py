person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]  # list whithin a dictionary
person["pets"] = {"dog": "Fido", "cat": "Sox"}  # dictionary within a dictionary

# print(person)
# print out the name of the second child

print(person["children"][1])

# print out the name of the cat

print(person["pets"]["cat"])

# iterate through all children and print out each child

for child in person["children"]:
    print(child)

# print out the pets in this format:

for i, j in person["pets"].items():
    print("Type of pets:", i, "Name of pets:", j)
