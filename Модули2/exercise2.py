import requests
import sys
flag = True

r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')

with open('answer2.txt', 'w') as file:
    file.write(r.text)

while flag:
    with open('answer2.txt', 'r') as file2:
        d = file2.readline().split()
    if d[0] == 'We':
        flag = False
        sys.exit()
    else:
        q = requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+d[0])
        with open('answer2.txt', 'w') as folder:
            folder.write(q.text)   
    
