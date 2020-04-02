import json

from django.views import generic
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Account

def sign_up(request):
    if request.method == "POST":
        account_name = request.POST.get('account_name')
        password = request.POST.get('password')
        Account(
            account_name = account_name,
            password = password
        ).save()
        return redirect(reverse('main:home'))

    return render(request, 'account/sign_up.html')

def login(request):
    if request.method == "POST":
        account_name = request.POST.get('account_name')
        password = request.POST.get('password')
        account = Account.objects.get(account_name=account_name)
        if account.password == password:
            request.session['account_name'] = account_name
        return redirect(reverse('main:home'))

    return render(request, 'account/login.html')

def logout(request):
    try:
        del request.session['account_name']
    except KeyError:
        pass
    return redirect(reverse('main:home'))