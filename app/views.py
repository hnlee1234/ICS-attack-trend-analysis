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
				parent = key[:4]
				if parent == '1000':
					key = key[4:]
				else:
					print("It is not started by 1000")
					pass
				ownid = key

				while True:
					if key[:3] == key[3:6]:
						parent = key[:3]
						key = key[6:]
					elif key[:2] == key[2:4]:
						parent = key[:2]
						key = key[4:]
					else:
						ownid = key
						break

				print(parent, ownid)
				new_node = Vulner.objects.create(id=ownid, name=val[0], parent=Vulner.objects.get(id=parent))
				new_node.save()
			except Exception as e:	
				print(e)
				print(ownid + " made some errors")
	
	context = {'vulners': Vulner.objects.all()}

	return render(request, 'main.html', context)