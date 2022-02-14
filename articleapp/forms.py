from dataclasses import fields
from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project

class ArticleCreationForm(ModelForm):
    
    # 프로젝트를 고르지 않아도 article 작성이 가능하도록
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']