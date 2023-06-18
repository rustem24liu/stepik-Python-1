with open("input.txt") as file:
    s = file.readline().strip()
some = []
first = []


string = ''
number = ''
result = ''

for i in range(len(s)):
    if s[i] > 'A':
        string = s[i]
        first.append(s[i])
        # print(string, end = " ")
    elif s[i] < 'A':
        number += s[i]
        # print(number, end = " ")
    # print(string, end = " ")
    # print(number, end = ' ')
    some.append(number)
    string = ''
    number = ''
# len_str = len(first)
# print(len_str)
for i in range(len(some)-1):
    if some[i].isdigit() and some[i+1].isdigit():
        some[i]= some[i] + some[i+1]
        some[i+1] = ''
for i in range(len(some)-1, -1, -1):
    if some[i] == '':
        some.pop(i)
    else:
        some[i] = int(some[i])
# print(first)
# print(some)
for i in range(len(first)):
    # print(first[i], some[i], end = ' ')
    result += first[i]*int(some[i])

with open("output.txt", "w") as out:
    out.write(result)




