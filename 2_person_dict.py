person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]  # list whithin a dictionary
person["pets"] = {"dog": "Fido", "cat": "Sox"}  # dictionary within a dictionary

print(person)

# print out the name of the second child

print(person["children"])

# print out the name of the cat

print(person["pets"])

# iterate through all children and print out each child


# print out the pets in this format:
# type of pet: dog name of pet: Fido
