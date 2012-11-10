from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify

class Votacion(models.Model):
    titulo = models.CharField(max_length=150, primary_key=True)
    activa = models.BooleanField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Votacion, self).save(*args, **kwargs)

admin.site.register(Votacion)

class Voto(models.Model):
    votacion = models.ForeignKey(Votacion)
    opcion = models.BooleanField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.votacion + " " + self.opcion

admin.site.register(Voto)
