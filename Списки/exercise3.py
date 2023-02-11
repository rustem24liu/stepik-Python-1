
arr = [int(i) for i in input().split()]
arr1 = sorted(arr)
res2 = []
res3 = {''}
res4 = []
def my_funct(arr1):
    res = 0
    cnt = 1
    current_char = arr1[0]
    ali = arr1[1:]
    for char in ali:
        if char == current_char:
            cnt+=1
            if cnt > 1:
                res2.append(char)
        else:
            current_char = char
            cnt = 1
            # if res > 1:
            #     res2.append(char)
    for r in res2:
            res3.add(r) 
    for t in res3:
            res4.append(t)
    res4.remove('')
    for y in res4:
        print(y, end = ' ')

    # for y in res2:
    #     print(y, end = " ")

my_funct(arr1)


