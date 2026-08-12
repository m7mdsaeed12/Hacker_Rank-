string = input()
substring = input()

count = 0

for i in range(len(string)):
    if string[i:i + len(substring)] == substring:
        print((i, i + len(substring) - 1))
        count += 1

if count == 0:
    print((-1, -1))