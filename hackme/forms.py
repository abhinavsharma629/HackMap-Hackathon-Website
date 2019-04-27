from .models import Register
from django import forms

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Register
		fields = ['teamName', 'emailAddress', 'github_username', 'project_repo_name', 'teamSize', 'userDetail1', 'userDetail2', 'userDetail3','fieldProject', 'title', 'synopsis']
