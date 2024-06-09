from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404

from custom_user.forms import CustomUserCreationForm, CustomUserAuthenticationForm, CustomUserChangeForm
from custom_user.models import CustomUser


def registration_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(username=form.cleaned_data['username'],
                                                  password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('complete_work')
        else:
            messages.info(request, f'{form.errors}')
            return render(request, 'register.html', {"form": CustomUserCreationForm})
    else:
        return render(request, 'register.html', {"form": CustomUserCreationForm})


def authenticate_user(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request.POST)
        user = CustomUser.objects.filter(username=form.request['username'])

        if user:
            if user[0].check_password(form.request['password']):
                login(request, user[0])

                return redirect('complete_work')
            else:
                messages.info(request, 'Invalid password')
                return render(request, 'authenticat.html', {'form': form})
        else:
            messages.info(request, 'Invalid username')
            return render(request, 'authenticat.html', {'form': form})

    else:
        form = CustomUserAuthenticationForm()
        return render(request, 'authenticat.html', {'form': form})


@login_required(login_url='authenticate')
def user_profile(request):
    form = CustomUserChangeForm
    user = get_object_or_404(CustomUser, pk=request.user.id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            hashed_phone_number = hash(phone_number)

            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.address = form.cleaned_data['address']
            user.phone_number = hashed_phone_number
            user.save()

            return redirect('profile')
        else:
            messages.info(request, f'{form.errors}')
            return redirect('profile')
    else:
        resp = {
            'login': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'address': user.address,
            'phone_number': user.phone_number,
            'form': form
        }
        return render(request, 'profile.html', resp)


def logout_user(request):
    user = request.user
    if user.is_authenticated:
        logout(request)

    return redirect('complete_work')
