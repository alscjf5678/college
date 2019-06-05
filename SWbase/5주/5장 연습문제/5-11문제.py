y=int(input("년도:"))
if y%4==0 and y%100!=0 or y%400==0:
    print("윤년")
else:
    print("평년")
