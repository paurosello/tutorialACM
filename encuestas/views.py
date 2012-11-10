# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def inicio(request):
    csrfContext = RequestContext(request)
    return render_to_response(
        'portada.html',
        {
        },
        csrfContext
    )