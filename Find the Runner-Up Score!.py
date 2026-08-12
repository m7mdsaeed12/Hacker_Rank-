n = int(input())
scores =list(map(int,input().split()))
new_list = []
for i in scores:
    if i not in new_list:
        new_list.append(i)
new_list.sort() # بيرتب من الصغير للكبير
print(new_list[-2])
