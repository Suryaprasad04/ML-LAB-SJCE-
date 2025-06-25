def data_operations():
    # List operations
    my_list = [3, 1, 4, 1, 5]
    my_list.append(9)             # Insert at end
    my_list.insert(2, 7)          # Insert at index 2
    my_list.remove(1)             # Delete first occurrence of 1
    my_list[0] = 8                # Update element at index 0
    print("Is 5 in list?", 5 in my_list)  # Search
    my_list.sort()
    print("List:", my_list)

    # Tuple (immutable, so we recreate)
    my_tuple = (10, 20, 30)
    print("Is 20 in tuple?", 20 in my_tuple)  # Search
    my_tuple = my_tuple + (40,)              # Insert (create new)
    print("Tuple:", my_tuple)

    # Set
    my_set = {1, 2, 3, 2}
    my_set.add(4)               # Insert
    my_set.discard(2)           # Delete
    print("Is 3 in set?", 3 in my_set)  # Search
    print("Set:", my_set)

    # Dictionary
    my_dict = {'a': 1, 'b': 2}
    my_dict['c'] = 3           # Insert
    my_dict['b'] = 5           # Update
    print("Is 'b' in dictionary?", 'b' in my_dict)  # Search
    del my_dict['a']           # Delete
    print("Dictionary:", my_dict)

data_operations()
