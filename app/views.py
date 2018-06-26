from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re
from app.models import Vulner, Company
#from .forms import VulnerModelForm
import csv

def main(request):
	req = requests.get('https://capec.mitre.org/data/definitions/1000.html')
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	attack = soup.find_all("a")
	content = dict()
	csv_dict = dict()
	
	#read csv file
	with open('app/2018-mitre-capec-filtered.csv', newline='', encoding = 'latin1') as csvfile:
		csvreader = csv.DictReader(csvfile)
		
		for l in csvreader:
			csv_dict[l['ID']] = l

	industry()
#	print(csv_dict['99']['Severity'])
	#create attacks' list with rough id after crawling
	for i in attack:
		if re.match('1000.' , str(i.get('name'))):
			content[i.get('name')] = i.contents

	with Vulner.objects.delay_mptt_updates():
		for key,val in content.items():
			try:
				#Level-1 cases
				parent = key[:4]
				if parent == '1000':
					key = key[4:]
				else:
					print("It is not started by 1000")
					pass
				ownid = key

				#Deeper level cases
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

				ownseverity = csv_dict[ownid]['Severity']

				new_node = Vulner.objects.create(id=ownid, name=val[0], severity = ownseverity, parent=Vulner.objects.get(id=parent))
				print(ownid + ": Created")
				new_node.save()

			except Exception as e:	
				if str(e) == "UNIQUE constraint failed: app_vulner.id":
					print(ownid, ": Duplicated")
					existing_node = Vulner.objects.get(id=ownid)
					#existing_node.id = ownid
					existing_node.severity = ownseverity
					existing_node.save()
				else:
					print(e)
				continue

	context = {'vulners': Vulner.objects.all()}

	return render(request, 'main.html', context)

def industry():
	tmp_dict = dict()
	
	#read csv file
	with open('app/list.csv', newline='', encoding = 'utf-8') as csvfile:
		csvreader = csv.DictReader(csvfile)
		
		for l in csvreader:
			tmp_dict[l['Company']] = l

		for com in tmp_dict.keys():
			try:
				new_node = Company.objects.create(name = com)
				new_node.save()
			except Exception as e:
				if str(e) == "UNIQUE constraint failed: app_Company.name":
					print(com, ": Duplicated")
				else:
					print(e)
				continue