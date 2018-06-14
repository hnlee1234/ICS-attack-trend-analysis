from django.shortcuts import render
from  treelib import Node, Tree
import requests
from bs4 import BeautifulSoup
import re

def main(request):
	req = requests.get('https://capec.mitre.org/data/definitions/1000.html')
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	attack = soup.find_all("a")
	content = dict()
	for i in attack:
		if re.match('1000.' , str(i.get('name'))):
			content[i.get('name')] = i.contents

	print(content)

	context = {'data' : content}
	return render(request, 'main.html', context)