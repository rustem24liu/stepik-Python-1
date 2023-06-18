lst = [1, 3,5, 7]


def modify_list(lst):
    for i in range(len(lst)-1, -1, -1):
        if lst[i]%2!=0:
            lst.pop(i)
    for i in range(len(lst)):
        lst[i]//=2
    
    print(lst)

modify_list(lst)
# modify_list(lst)