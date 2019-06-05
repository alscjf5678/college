issn=input("ISSN 8자리(-제외):")
sum=0
for i in range(len(issn)-1):
    weight=8-i
    sum+=int(issn[i])*weight
n=sum%11
check_num=11-n
print("ISSN 1~7자리의 가중치 반영합계:",sum)
if check_num==10:
    check_num='X'
elif check_num==11:
    check_num='O'
print("ISSN 1~7자리의 체크기호 값:",check_num)
if issn[7].isdigit():
    if check_num==int(issn[7]):
        print("ISSN 코드:",issn+"은(는) 검증되었습니다.")
    else:
        print("ISSN 코드:",issn+"은(는) 검증되지 않았습니다.")
else:
    if check_num==issn[7]:
        print("ISSN 코드:",issn+"은(는) 검증되었습니다.")
    else:
        print("ISSN 코드:",issn+"은(는) 검증되지 않았습니다.")
