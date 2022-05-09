

str1 = "Shubham is great"
str2 = "is"
print(str1)  # printing the str1

print(str1[0:4])  # Shub, from index 0 to 3(4-1)
print(str1[-1])  # t, will print the last index

# check whether a string is present in another or not
isPresent = str2 in str1  # it will return true is present and false if not
print(isPresent)

# split string

splitted = str1.split(" ")
print(splitted)   # ['Shubham', 'is', 'great'], it will split the string on space and store in a list

# if we want to extract suppose Shubham from the splitted string, them simply splitted[0]
for i in splitted:  # iterating over the list and printing each index
    print(i)


# trim exapmle
# strip() is an inbuilt function in Python programming language that returns a copy of the string with both leading
# and trailing characters removed (based on the string argument passed).
str4 = "grgeaggggtggggg"
trimmed = str4.strip("g")
print(trimmed)  # rgeaggggt, it removed all the g from leading and trailing end from the string


# trim only from the leading end

print(str4.lstrip("g"))  # rgeaggggtggggg, removed all g from the leading end
# similarly rstrip for the trailing end
