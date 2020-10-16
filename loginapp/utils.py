from django.shortcuts import render, redirect
from .models import User, Quote

def check_for_methodPOST(request):
    if request.method != 'POST':
        return redirect('/')


def check_for_user(request):
    if not 'userid' in request.session:
        return redirect('/')
    else:
        global logged_in_user
        logged_in_user = User.objects.get(email=request.session['userid'])