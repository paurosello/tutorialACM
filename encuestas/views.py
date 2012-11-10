# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from encuestas.models import Votacion

def inicio(request):
    csrfContext = RequestContext(request)
    return render_to_response(
        'portada.html',
        {
            'votaciones' : Votacion.objects.all()
        },
        csrfContext
    )