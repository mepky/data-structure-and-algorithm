import requests 
  
# api-endpoint 
r = requests.get('https://api.github.com/events')
r = requests.post('https://httpbin.org/post', data = {'name':'Joe'})
r = requests.put('https://httpbin.org/put', data = {'name':'Joe'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)


payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('https://httpbin.org/get', params=payload)
print('URL: ', r.url)
print('ENCODING: ', r.encoding)
print('STATUS_CODE: ', r.status_code)
print('HEADERS: ', r.headers)
print('TEXT: ', r.text)
print('CONTENT: ', r.content)
print('JSON: ', r.json)


r = requests.post('https://httpbin.org/post', data = {'name':'Joe'})

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)