n = input()
n = n.upper()
res1 = n.count("C")
res2 = n.count("G")
res3 = res1+res2
print(float(res3/len(n)*100))