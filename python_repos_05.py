import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code :' , r.status_code)

#将API响应存储在一个变量之中
response_dict = r.json()

#处理结果
print('Total repositories :', response_dict['total_count'])

#搜索有关仓库的信息
repo_dicts = response_dict['items']

names , stars = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

#可视化
my_style = LS('#333366' ,base_style = LCS)

my_config = pygal.Config()
my_config.x_labels_rotation = 45
my_configimport requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code :' , r.status_code)

#将API响应存储在一个变量之中
response_dict = r.json()

#处理结果
print('Total repositories :', response_dict['total_count'])

#搜索有关仓库的信息
repo_dicts = response_dict['items']

names , stars = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

#可视化
my_style = LS('#333366' ,base_style = LCS)
chart = pygal.Bar(style = my_style , x_labels_rotation = 45 ,show_legend = False)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('',stars)
chart.render_to_file('python_repos.svg')
my_config.show_legend =False
my_config.title_front_size = 24
my_config.label_front_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides =False
my_config.width = 1000

chart = pygal.Bar(my_config , style = my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('',stars)
chart.render_to_file('python_repos.svg')
