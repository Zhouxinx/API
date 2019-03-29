import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code :' , r.status_code)

#将API响应存储在一个变量之中
response_dict = r.json()

#处理结果
print(response_dict.keys())
