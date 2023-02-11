a = input() # for this task I creat a function that returns us our result

def my_func(a): # -> for example a = 'aaaabbcaa'
    res = ''
    cnt = 1
    current_char = a[0] # -> current_char = 'a'
    ali = a[1:] # -> ali = 'aaabbcaa' {without one a}
    for char in ali:
        if char == current_char: # -> if a == a || if a == a || if a == a || if a != b -> it goes to else:
            cnt+=1 # -> every time if char and current_char are equals cnt will increasing
        else:
            res+= current_char+str(cnt) # -> it gives us our finall string
            current_char = char # -> for next loop we change variable of current_char for ex: in the next loop current_char = 'b'
            cnt = 1 # -> and value of cnt will equal = 1 because for the next loop it starts again
    res+=current_char + str(cnt) # -> it is also finall result
    print(res)

my_func(a)
