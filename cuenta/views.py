# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout


def login_agrocal(request):
    if request.method == 'GET':

		return render_to_response('account_login.html',{},context_instance=RequestContext(request))
    elif request.method == 'POST':
        ddic = {}
        username = request.POST.get('user','')
        password = request.POST.get('password','')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('main')
            else:
                ddic['error'] = {'message':'Cuenta Deshabilitada.'}
                return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
        else:
            ddic['error'] = {'message':u'Acceso Inválido.'}
            return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))

#def get_perms(user):

def logout_agrocal(request):
    ddic = {}
    logout(request)

    return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
