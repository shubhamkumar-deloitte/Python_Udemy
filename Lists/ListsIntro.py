
# defining a list
lst = [1, 3, "value", 3.445, "Shubham", 22, "Bihar"]
print(lst)

# accessing the list element
print(lst[0])

# print the last element of the list
print(lst[-1])  # 3.445

# extract or print a portion of the list
# syntax is lst[staring_index:last_index]
# The last index is exclusive, it will print till last_index-1
print(lst[0:3])  # 1 3 value, and the last_index '3' got excluded

# print from the 0th index to the last_index-1
print(lst[:-1])  # [1, 3, 'value', 3.445, 'Shubham', 22]
