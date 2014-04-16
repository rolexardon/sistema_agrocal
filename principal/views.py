from django.shortcuts import render, render_to_response
from django.template import RequestContext

def main(request):
    ddic = {}
    print 'voy'
    if not request.user.is_authenticated():
        return render_to_response('account_login.html',ddic,context_instance=RequestContext(request))
    return render_to_response('main.html',ddic,context_instance=RequestContext(request))

