

lst = [1, 2, 3, 4, 5, 6, 67, "skdhb"]  # list

# iterate the list
for i in lst:
    print(type(i), i)

# totalSum of first five natural numbers
totalSum = 0
for i in range(1, 6):
    totalSum += i
    print(i)  # 1 2 3 4 5
print("final totalSum is ", totalSum)

# increase the iteration speed by two instead of one
# the third argument is to define the speed
for i in range(1, 6, 2):
    print(i)  # 1 3 5
print("****************************************")
for i in range(10):
    print(i)  # from 0 to 9
