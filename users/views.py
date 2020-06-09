from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token


#  class SignUp(CreateView):
#    form_class = CustomUserCreationForm
#    success_url = reverse_lazy('login')
#    template_name = 'signup.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your slack underflow site'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
