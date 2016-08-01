import http.client

client = http.client.HTTPConnection('www.google.com')
client.request('GET', '/')
res = client.getresponse()
print(res.read().decode('utf-8'))
