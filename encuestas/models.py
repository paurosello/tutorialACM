from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify

class Votacion(models.Model):
    titulo = models.CharField(max_length=150)
    activa = models.BooleanField(default=True)
    fecha = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)

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

        return self.votacion.titulo + " " + str(self.opcion)

admin.site.register(Voto)
