from django.http import HttpResponseForbidden

from profileapp.models import Profile

def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        #본인인지 확인하는 작업
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user==request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated
        