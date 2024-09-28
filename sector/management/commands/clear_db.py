import os
from PIL import Image
from django.core.files import File
from django.core.management.base import BaseCommand
from faker import Faker
from sector.models import Sector, Banner

class Command(BaseCommand):
    help = 'Limpar todos os setores e banners'

    def handle(self, *args, **kwargs):
        Banner.objects.all().delete()
        Sector.objects.all().delete()