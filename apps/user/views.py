from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from apps.user.forms import LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def user_login(request):
    error = None
    next_page = request.GET.get('next', reverse('home'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(next_page)
                else:
                    error = 'Вы забанены, идите лесом -->'
            else:
                error = 'Неправильные логин или пароль'
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form, 'error': error})


def user_logout(request):
    logout(request)
    return redirect('home')
