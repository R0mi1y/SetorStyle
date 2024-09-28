from django.db import models
from django.template.loader import render_to_string
from django.core.validators import MinValueValidator, MaxValueValidator

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
    JUSTIFY_CHOICES = [
        ("flex-start", "Início"),
        ("flex-end", "Fim"),
        ("center", "Centro"),
        ("space-between", "Espaçamento entre"),
        ("space-around", "Espaçamento ao redor"),
        ("space-evenly", "Espaçamento igual"),
    ]

    ALIGN_CHOICES = [
        ("flex-start", "Início"),
        ("flex-end", "Fim"),
        ("center", "Centro"),
    ]
    
    title = models.CharField("Titulo", max_length=255)
    description = models.TextField("Descricão", max_length=500)
    image = models.ImageField("Imagem", upload_to='banners/')
    justify = models.TextField("Alinhamento vertical", choices=JUSTIFY_CHOICES, default=JUSTIFY_CHOICES[0][0])
    align = models.TextField("Alinhamento horizontal", choices=ALIGN_CHOICES, default=ALIGN_CHOICES[0][0])
    padding = models.IntegerField("Espaçamento interno (%)", default=0, validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ])
    size_title = models.IntegerField("Tamanho do titulo", default=50, validators=[
            MinValueValidator(0),
        ])
    size_description = models.IntegerField("Tamanho da descrição", default=20, validators=[
            MinValueValidator(0),
        ])
    width = models.IntegerField("Largura do texto (%)", default=90, validators=[
            MinValueValidator(10),
            MaxValueValidator(100),
        ])
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
    
    
    def get_presentation(self):
        return render_to_string('banners/banner_base.html', {'banner': self})