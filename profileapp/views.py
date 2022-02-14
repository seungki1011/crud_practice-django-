from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from profileapp.decorators import profile_ownership_required

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    #프로필을 생성 후 detail 페이지로 이동하게 설정은 reverse_lazy로 불가능, 왜냐하면 pk를 넘겨줘야하기 때문
    #내부 메서드를 하나 만들어서 detail로 가도록 만들거임
    #success_url = reverse_lazy('accountapp:detail')
    template_name = 'profileapp/create.html'
    
    # user field를 서버쪽에서 처리하도록
    def form_valid(self, form): #forms.py에서 날라온 데이터를 form에서 받음
        temp_profile = form.save(commit=False) # temp_profile에 임시로 저장 (실제 db에는 저장안함)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
    

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})