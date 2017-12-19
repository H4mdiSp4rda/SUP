from django import forms

from .models import Course

class AddCourse(forms.Form):
	title 			= forms.CharField(required=True)
	file 			= forms.FileField()
	description 	= forms.CharField(required=True, help_text='Please enter a brief description of the course.')
