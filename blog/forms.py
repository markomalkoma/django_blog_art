from django import forms 
from .models import Comment, Subcomment

class CommentForm(forms.Form):
	content=forms.CharField()
	

class SubcommentForm(forms.Form):
	content=forms.CharField()
	