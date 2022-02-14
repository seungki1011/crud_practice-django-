from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    # profile과 detail 1:1 매칭
    # profile과 User객체를 1:1로 연결해준다 , User객체가 delete 되면 profile도 delete
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') 
    
    # media 루트 아래에 profile 이라는 경로가 추가되어서 업로드됨
    # null = True : 프로필 사진이 없어도 괜찮다
    image = models.ImageField(upload_to = 'profile/', null=True)
    
    # unique=True : 프로필의 닉네임은 유일하다
    # null = True : 설정이 되지 않았다면 닉네임을 설정해달라는 메세지 뛰우는 방식으로 구현할거임, 보통은 null=False
    nickname = models.CharField(max_length=20, unique=True, null=True)
    
    # 상태 메세지
    message = models.CharField(max_length=100, null=True)

    # profile form은 장고에서 기본제공 하지 않기 때문에 만들어야함
    # form을 일일이 다 만들기 힘들기 때문에 Model Form 사용
    # model form은 기존의 model을 form으로 변환 해주는 기능