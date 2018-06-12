from django.shortcuts import render, redirect


import random
import time
import datetime
import json



# 사료 구매 / 고기 구매
def main(request):
	return render(request, "main.html")

