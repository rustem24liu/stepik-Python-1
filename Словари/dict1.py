def update_dictionary(d, key, value):
    if key in d:
        d[key]+=[value]
    elif 2*key in d:
        d[2*key]+=[value]
    else:
        d[2*key]=[value]
d={}
(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)
update_dictionary(d, 3, 0)
print(d)