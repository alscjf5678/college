import time
now=time.localtime() 
a=input("주민등록번호 년월일:")
b=input("당신이 태어난 년대[ex)1900,2000]:")
print("나이:",now.tm_year-(int(a[0:2])+int(b))+1)
