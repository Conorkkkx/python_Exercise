#_*_coding:utf-8_*_

a = 0
b = 1
i = 1
print(a,end=",")
while i<10:
    b = a + b
    a = b - a
    i += 1
    print(a,end = ",")
    
