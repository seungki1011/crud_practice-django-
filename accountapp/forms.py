from django.contrib.auth.forms import UserCreationForm

# form custamizing 할거임

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # username 창이 disabled 됨
        self.fields['username'].disabled = True