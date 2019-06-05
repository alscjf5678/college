data =[[21,7,43,65],[2,8,72,52]]
a=int(input("찾을 값:"))

for i in range(len(data)):
    if a in data[i]:
        break
for j in range(len(data[i])):
    if a==data[i][j]:
        break
if a==data[i][j]:
    print("위치:",i+1,"행",j+1,"열")
else:
    print("찾지 못함")
