a=input("문자열:")
while 1:
    b=input("문자:")
    if b=="":
        break
    elif b not in a:
        print("문자",b+"가 문자열",a+"에 존재하지 않음")
    elif b in a:
        print("문자",b+"가 문자열",a+"에 존재함")
