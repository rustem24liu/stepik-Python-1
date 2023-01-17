x = int(input())
h = int(input())
m = int(input())
a = x/60
b = abs(int(a)*60-x)
resultH = h+int(a)
resultM = m+int(b)
if resultM > 60 :
    c = int(resultM/60) + resultH
    d = resultM -60 
    print(int(c))
    print(int(d))
else:
    print(resultH)
    print(resultM)
