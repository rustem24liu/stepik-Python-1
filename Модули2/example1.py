import requests

r = requests.get('https://ru.wikipedia.org/wiki/%D0%A5%D1%8C%D1%8E%D1%81%D1%82%D0%BE%D0%BD')
print(r.text)

url = 'https://ru.wikipedia.org/wiki/%D0%A5%D1%8C%D1%8E%D1%81%D1%82%D0%BE%D0%BD'
par = {'key': 'value', 'key2': 'value2', 'key3': 'value3'}
r = requests.get(url, params=par)
print(r.url)

url = 'https://httpbin.org/cookies'
cookies = {'cookies_are':'working', 'my_name':'liu_rus'}
r = requests.get(url, cookies=cookies)
print(r.text)

print(r.cookies['my_name'])

