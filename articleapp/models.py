from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project

# Create your models here.


class Article(models.Model):
    # 글쓴이가 회원 탈퇴할경우 글쓴이가 알수 없음형태로 뜨도록
    # 유저 객체에서 접근할때 사용할 이름 article
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    
    created_at = models.DateField(auto_now_add=True, null=True)