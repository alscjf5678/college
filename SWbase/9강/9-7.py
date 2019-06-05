data=[21,7,43,65,2,8,72,9]
a=int(input("찾을 값:"))
for i in range(len(data)):
    if a in data:
        if a==data[i]:
            break
    else:
        break
    
if a in data:
    print("위치:",i)
else:
    print("찾지 못함")
