from django.urls import path
from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accountapp'

urlpatterns = [
    
    #로그인, 로그아웃은 간단해서 view에서 설정안하고 url에서 바로
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # cbv는 as_view() 붙여줌
    path('create/', AccountCreateView.as_view(), name='create'), 
    # detail은 유저정보를 보는것, id(primary key) 필요
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'), 
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'), 
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'), 
]
