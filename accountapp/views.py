from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import MultipleObjectMixin

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm

from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]


# Create your views here.

# 계정 생성 뷰, CreateView 상속 받음
# 장고에서 기본 제공하는 User라는 모델사용
# form도 기본 제공됨
# 계정만들기에 성공하면 어느 url로 다시 연결해줄건지 설정
# class view 에서 url redirect 할때 reverse_lazy 사용해야함
# 회원가입 할 때 사용할 template 설정

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "accountapp/create.html"
    

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
    
    paginate_by = 8
    
    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)
    

# method_decorator는 일반함수에서 사용하는 decorator를 class(method)에서 사용가능하게 함
# login_required는 customization 필요(custom decorator 만들어서)
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy("home")
    template_name = "accountapp/update.html"
    
    
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy("accountapp:login")
    template_name = "accountapp/delete.html"
    