# List operations
my_list = [1, 2, 3]
print("Original list:", my_list)

# Adding elements
my_list.append(4)
print("After appending 4 to the list:", my_list)

# Removing elements
my_list.remove(2)
print("After removing 2 from the list:", my_list)

# Modifying elements
my_list[1] = 10
print("After changing the second element to 10:", my_list)

# Dictionary operations
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nOriginal dictionary:", my_dict)

# Adding elements
my_dict['d'] = 4
print("After adding key 'd' with value 4 to the dictionary:", my_dict)

# Removing elements
del my_dict['b']
print("After removing key 'b' from the dictionary:", my_dict)

# Modifying elements
my_dict['a'] = 10
print("After changing the value of key 'a' to 10:", my_dict)

# Set operations
my_set = {1, 2, 3}
print("\nOriginal set:", my_set)

# Adding elements
my_set.add(4)
print("After adding 4 to the set:", my_set)

# Removing elements
my_set.remove(2)
print("After removing 2 from the set:", my_set)

# Modifying elements
# Note: Sets do not support direct modification of elements,
# so we need to remove and add if we want to change a value
my_set.discard(1)  # Removing 1
my_set.add(10)     # Adding 10
print("After removing 1 and adding 10 to the set:", my_set)
