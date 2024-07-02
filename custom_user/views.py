from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

import json

from custom_user.forms import CustomUserCreationForm, CustomUserAuthenticationForm, CustomUserChangeForm
from custom_user.models import CustomUser
from custom_user.my_requests import get_request, post_request


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
        form = CustomUserChangeForm(request.POST)
        if form.is_valid():

            if form.cleaned_data['phone_number']:
                '''
                request to write a phone number to the database (the request is sent by the "post_request" function)
                '''
                phone_number = form.cleaned_data['phone_number']
                hashed_phone_number = hash(phone_number)

                data = json.dumps({'hashed_phone_number': str(hashed_phone_number), 'phone_number': str(phone_number)})

                post_request(data)

                user.phone_number = hashed_phone_number

            if form.cleaned_data['first_name']:
                user.first_name = form.cleaned_data['first_name']

            if form.cleaned_data['last_name']:
                user.last_name = form.cleaned_data['last_name']

            if form.cleaned_data['email']:
                user.email = form.cleaned_data['email']

            if form.cleaned_data['address']:
                user.address = form.cleaned_data['address']

            user.save()

            return redirect('profile')
        else:
            messages.info(request, f'{form.errors}')
            return redirect('profile')
    else:
        phone_number = ''
        if not user.address:
            address = ''
        else:
            address = user.address

        if user.phone_number is not None:
            '''
            request to get a phone number by hash from another application 
            (the request is sent by the "get_request" function)
            '''
            params = {'hashed_phone_number': str(request.user.phone_number)}
            get_response = get_request(params)

            if get_response.status_code == 200:
                phone_number = get_response.json()['phone_numbers']

        resp = {
            'login': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'address': address,
            'phone_number': phone_number,
            'form': form
        }
        return render(request, 'profile.html', resp)


def logout_user(request):
    user = request.user
    if user.is_authenticated:
        logout(request)

    return redirect('complete_work')
