from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import RegistrationForm
from django.utils import timezone
from django.db.models import Q

def main(request):
	return render(request, 'hackme/main2.html')


def form(request):
	return render(request, 'hackme/formBackground.html')

def form1(request):
	if(request.method=='POST'):
		print(request)
		form=RegistrationForm(request.POST)
		if(form.is_valid()):
			form.save()

			team=request.POST.get('teamName')
			return render(request, 'hackme/cform.html', {'detail':team})

	else:
		form=RegistrationForm()
	return render(request, 'hackme/cform.html', {'form':form})

def contact(request):
	if(request.method=='POST'):

		form=ContactForm(request.POST)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect('/contact')
	else:
		form=ContactForm()
	return render(request, 'hackme/cform.html', {'form':form})


def detail(request, details):
	teamdetails=Register.objects.filter(Q(teamName=details))
	timer=timezone.now()
	f=str(timer).split(" ")
	time=f[1]
	time=str(time).split(":")
	h=str(((int)(time[0])))
	m=str(((int)(time[1])))
	
	return render(request, 'hackme/detail.html', {'timer':h+":"+m+":"+time[2].split(".")[0], 'teamName':teamdetails})