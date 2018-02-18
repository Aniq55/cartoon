from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import models
from django.contrib import messages
from level import models
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
# from facepy import GraphAPI
import datetime
import time

m_level = 1
f_user = ""
last = 2

def index(request):
	return render(request,'index.html')

def page_1(request):
	user = request.user
	if user.is_authenticated():
		player = models.player.objects.get(user_id=request.user.pk)
        try:
            level = models.level.objects.get(l_number=player.max_level)
            return render(request, 'level.html', {'player': player, 'level': level})
        except:
            global last
            if player.max_level > last:
                return render(request, 'win.html', {'player': player})
            return render(request, 'finish.html', {'player': player})
	return render(request,'page_1.html')		

def page_2(request):
	return render(request,'page_2.html')	

def leaderboard(request):
	return render(request,'leaderboard.html')

def level_1(request):
	return render(request,'l_1.html')				
