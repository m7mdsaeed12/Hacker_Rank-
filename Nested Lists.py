n = int(input())
list1 = []
grades = []
names = []

for i in range(n):
    name = input()
    score = float(input())

    list1.append([name, score])

for i in range(n):
    if list1[i][1] not in grades:
        grades.append(list1[i][1])

grades.sort()

for i in range(n):
    if grades[1] == list1[i][1]:
        names.append(list1[i][0])

names.sort()

for name in names:
    print(name)