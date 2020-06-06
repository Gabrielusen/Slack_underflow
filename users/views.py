from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth import login, authenticate


#  class SignUp(CreateView):
#    form_class = CustomUserCreationForm
#    success_url = reverse_lazy('login')
#    template_name = 'signup.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
