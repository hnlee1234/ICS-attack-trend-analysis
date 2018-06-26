from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re
from app.models import Vulner, Company, Product
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
	with open('log.txt','w') as logfile:
		for i,j in csv_dict.items():
			logfile.write(i+'\n')

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

				if parent == str(1000):
					Vulner.objects.update_or_create(id=ownid, name=val[0], severity = "", parent=Vulner.objects.get(id=parent))	

				else:
					ownseverity = csv_dict[ownid]['Severity']
					#print(parent, ownid)
					Vulner.objects.update_or_create(id=ownid, name=val[0], severity = ownseverity, parent=Vulner.objects.get(id=parent))
				
				print(ownid + ": Update/Created")

			except Exception as e:	
				print(e)
				continue

	context = {'vulners': Vulner.objects.all()}

	return render(request, 'main.html', context)

def industry():
	tmp_dict = dict()
	
	#read csv file
	with open('app/list.csv', newline='', encoding = 'utf-8') as csvfilei:
		csvreaderi = csv.DictReader(csvfilei)
		
		for l in csvreaderi:
			tmp_dict[l['Company']] = l

		for k,v in tmp_dict.items():
			try:
				Company.objects.update_or_create(name = k, url = v['URL'], parent=None)
				Product.objects.update_or_create(name = v['Product/Service'], company = Company.objects.get(name=k),
    				paper1 = v['Paper1'], paper2 = v['Paper2'], refer = v['reference'], relation_level = v['relation level'],
    				main_division = v['Company division'], sub_division = v['subdivision'])
			except Exception as e:
				print(e)
				continue