from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re
from app.models import Vulner
from .forms import VulnerModelForm


def main(request):
	req = requests.get('https://capec.mitre.org/data/definitions/1000.html')
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	attack = soup.find_all("a")
	content = dict()
	for i in attack:
		if re.match('1000.' , str(i.get('name'))):
			content[i.get('name')] = i.contents


	with Vulner.objects.delay_mptt_updates():
		for key,val in content.items():
			try:
				#Normal cases
				print(key[-3:])
				new_node = Vulner.objects.create(id=str(key[-3:]), name=val[0], parent=Vulner.objects.get(id=str(key[-6:-3])))
				new_node.save()
				#new_node = Vulner.objects.insert_node()
			except:
				try:
					#'Root is 1000' cases
					print(key[-3:])
					new_node = Vulner.objects.create(id=str(key[-3:]), name=val[0], parent=Vulner.objects.get(id=str(key[0:4])))
					new_node.save()
				except:
					try:
						#'xx' cases (not '0xx')
						print(key[-2:])
						new_node = Vulner.objects.create(id='0'+str(key[-2:]), name=val[0], parent=Vulner.objects.get(id=str(key[-5:-2])))
						new_node.save()
					except Exception as e:	
						print(e)
						print(key[-3:] + "made some errors")
	
	context = {'data' : content, 'vulners': Vulner.objects.all()}

	return render(request, 'main.html', context)