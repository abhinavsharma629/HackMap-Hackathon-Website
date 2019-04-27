from django.db import models
from django.contrib import admin

class Register(models.Model):
	#id_1=models.UUIDField(default=uuid.uuid4, editable=True)
	CHOICES=(
		(1,'1'),
		(2,'2'),
		(3,'3'),
		)
	teamName=models.CharField(primary_key=True,max_length=100, null=False, blank=False)
	emailAddress=models.EmailField(null=False)
	github_username=models.CharField(max_length=150, null=False, blank=False)
	project_repo_name=models.CharField(max_length=150, null=False, blank=False)
	teamSize=models.IntegerField(choices=CHOICES)
	userDetail1=models.CharField(max_length=150, null=False, blank=False)
	userDetail2=models.CharField(max_length=150,blank=True,null=True)
	userDetail3=models.CharField(max_length=150,blank=True,null=True)
	fieldProject=models.CharField(max_length=30,null=False, blank=False)
	title=models.CharField(max_length=50,null=False, blank=False)
	synopsis=models.TextField(null=False, blank=False)
