s = input()
i = 0
j = len(s)-1
is_polindrom = False
while i < j:
    if s[i] == s[j]:
        is_polindrom = True
    else:
        is_polindrom = False
    i+=1
    j-=1

if is_polindrom:
    print("YES")
else:
    print("NO")