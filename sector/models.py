from django.db import models
from django.template.loader import render_to_string

class Sector(models.Model):
    name = models.CharField("Nome", max_length=255, unique=True)
    description = models.TextField("Descricão", max_length=500)
    banners = models.ManyToManyField('Banner')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
    
    
class Banner(models.Model):
    title = models.CharField("Titulo", max_length=255)
    description = models.TextField("Descricão", max_length=500)
    image = models.ImageField("Imagem", upload_to='banners/')
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
    
    
    def get_presentation(self):
        return render_to_string('banners/banner_base.html', {'banner': self})