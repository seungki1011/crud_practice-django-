from django.forms import ModelForm

from profileapp.models import Profile

class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message'] # user필드는 서버에서 처리할거임