def div_qr():
    x=int(input())
    y=int(input())
    a=x//y
    b=x%y
    return(a,b)
(c,d)=div_qr()
print("몫 :",c,"나머지 :",d)
