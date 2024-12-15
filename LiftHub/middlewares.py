from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if (hasattr(request.user, 'profile') and not request.user.profile.is_completed
                    and not request.user.is_superuser):

                setup_url = reverse('profile-edit', kwargs={'slug': request.user.profile.slug})
                logout_url = reverse('logout')
                if request.path != setup_url and request.path != logout_url:
                    return redirect(setup_url)

        return self.get_response(request)
