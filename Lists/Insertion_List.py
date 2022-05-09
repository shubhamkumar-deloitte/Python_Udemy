
lst = [1, 2, 3, "Shubham", "Bihar", 22, "SUIT"]
print(lst)  # [1, 2, 3, 'Shubham', 'Bihar', 22, 'SUIT']

# insertion at any index lst.insert(index,value)
lst.insert(3, "New_Insertion")
print(lst)  # [1, 2, 3, 'New_Insertion', 'Shubham', 'Bihar', 22, 'SUIT']

# insertion at the last of the list
lst.append("lastValue")
print(lst)  # [1, 2, 3, 'New_Insertion', 'Shubham', 'Bihar', 22, 'SUIT', 'lastValue']

# updating the value in the list
lst[4] = "SHUBHAM"
print(lst)  # [1, 2, 3, 'New_Insertion', 'SHUBHAM', 'Bihar', 22, 'SUIT', 'lastValue']

# delete the value from the list
del lst[4]
print(lst)  # [1, 2, 3, 'New_Insertion', 'Bihar', 22, 'SUIT', 'lastValue']
