# tuple are immutable, we cannot update it once it is declared unlike lists

val = (1, 2, 3, "Shubham")
print(val)
print(val[0])  # 1

# trying to update
val[2] = "mew"  # 'tuple' object does not support item assignment
