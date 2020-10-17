import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.xxxxx.com/'
next_url = url

for i in range(5):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	link_list = soup.find_all('a')

	print(f'page:{i+1}')
	print(f'url:{url}')

	if not link_list:
		print('link_list is empty')
		break

	for link in link_list:
		next_url = link.get('href')

		if not re.match((r'https://'), next_url):
			continue

		if url != next_url:
			break

	if url == next_url:
		print('url and next_url are the same')
		break

	url = next_url