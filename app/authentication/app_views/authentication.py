# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.contrib import messages


@require_http_methods(['GET', 'POST'])
def signin(request):
    if request.user.is_authenticated:
        return redirect('dashboard:garden_monitoring')
    else:
        if request.POST:
            if AuthenticationForm(request.POST or None).is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)                        
                        request.session['user_id'] = user.id                        
                        return redirect('dashboard:garden_monitoring')
                    else:
                        messages.add_message(request, messages.ERROR, 'Akun anda telah di cekal!, silahkan hubungi bagian bagian administrasi.')
                else:
                    messages.add_message(request, messages.WARNING, 'Password atau Nomor Induk tidak cocok!')
            else:
                messages.add_message(request, messages.WARNING, 'Silahkan isi dengan lengkap form dibawah!')
        return render(request, template_name='base/authentication/signin.html')
    

@login_required
@require_http_methods(['GET'])
def signout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.INFO, 'Anda berhasil logout!')
    return redirect('authentication:signin')
