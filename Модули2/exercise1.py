import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/747.txt')
len = len(r.text.splitlines())


with open('output.txt', 'w') as out:
   out.write(str(len))

with open('input.txt', 'r') as file:
   d = file.readline().split( )
print(d[0])
   

    