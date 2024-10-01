# List Operations
my_list = [1, 2, 3, 4, 5]
print("Initial List:", my_list)

# Adding an element to the list
my_list.append(6)
print("List after adding an element:", my_list)

# Removing an element from the list
my_list.remove(2)
print("List after removing an element:", my_list)

# Modifying an element in the list
my_list[2] = 10  # Modifies the third element (index 2)
print("List after modifying an element:", my_list)


# Dictionary Operations
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nInitial Dictionary:", my_dict)

# Adding a key-value pair
my_dict['d'] = 4
print("Dictionary after adding a key-value pair:", my_dict)

# Removing a key-value pair
del my_dict['b']
print("Dictionary after removing a key-value pair:", my_dict)

# Modifying a value in the dictionary
my_dict['a'] = 10
print("Dictionary after modifying a value:", my_dict)


# Set Operations
my_set = {1, 2, 3, 4, 5}
print("\nInitial Set:", my_set)

# Adding an element to the set
my_set.add(6)
print("Set after adding an element:", my_set)

# Removing an element from the set
my_set.remove(3)
print("Set after removing an element:", my_set)

# Modifying a set
my_set.discard(4)  # Remove an element
my_set.add(10)     # Add a new element
print("Set after modifying (indirect modification):", my_set)
