def str2int(a):
    if a.isdigit():
        return a
    else:
        return "None"
b=input("문자열:")
print(str2int(b))
