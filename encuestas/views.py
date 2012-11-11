# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from encuestas.models import Votacion, Voto

def inicio(request):
    return render_to_response(
        'portada.html',
        {
            'votaciones' : Votacion.objects.all()
        },
    )

def activas(request):
    votaciones = Votacion.objects.filter(activa=True)

    return render_to_response(

        'portada.html',
        {
            'nvotaciones' : votaciones.count(),
            'votaciones' : votaciones
        },
    )

def realizar_voto(request, votacion, voto):

    votacion_act = Votacion.objects.get(pk=votacion)

    voto_realizado=None
    if(votacion_act.activa):
        voto_realizado = Voto(votacion=votacion_act, opcion=int(voto)==1)
        voto_realizado.save()

    return render_to_response(
        'voto_realizado.html',
        {
            'voto':voto_realizado
        },
    )

def votacion(request, vot_id):
    rvotacion = Votacion.objects.get(pk=vot_id)

    votos = Voto.objects.filter(votacion=rvotacion)

    return render_to_response(
        'votacion.html',
        {
            'votacion' : rvotacion,
            'votosFavor' : votos.filter(opcion=True),
            'votosContra' : votos.exclude(opcion=True)
        },
    )


from django.forms import ModelForm
class ArticleForm(ModelForm):
    class Meta:
        model = Votacion
        fields = ('titulo', 'activa')

def nueva_votacion(request):
    contexto = RequestContext(request)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response("nueva_votacion.html", {
            })
    else:
        form = ArticleForm()

    return render_to_response("nueva_votacion.html", {
        "form": form,
        },
    contexto)