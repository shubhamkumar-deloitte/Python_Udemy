

it = 4

while it > 1:
    print(it)  # 4 3 2
    it -= 1

# don't print when it=3
it = 4
while it > 1:
    if it != 3:
        print(it)  # 4 2
    it -= 1

