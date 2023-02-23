def modify_list(l):
    i = 0
    while i < len(l):
        if l[i] % 2 == 0:
            l[i] //= 2
            i += 1
        else:
            del l[i]
        return l
# arr = [1,2,3,4,5,6]
# (modify_list(arr))
# print(arr)
# # print(modify_list(arr))