import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code :' , r.status_code)

#将API响应存储在一个变量之中
response_dict = r.json()

#处理结果
print('Total repositories :' , response_dict['total_count'])

#搜索有关仓库的信息
repo_dicts = response_dict['items']
print('repositories returned: ' , len(repo_dicts))

#研究第一个仓库

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
	print('\nName:' , repo_dict['name'])
	print('Owner:' , repo_dict['owner']['login'])
	print('Stars:' , repo_dict['stargazers_count'])
	print('Repositories' , repo_dict['html_url'])
	print('Created:' , repo_dict['created_at'])
	print('Updated:' , repo_dict['updated_at'])
	print('Description:' , repo_dict['description'])
