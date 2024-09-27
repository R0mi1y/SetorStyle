import os
from PIL import Image
from django.core.files import File
from django.core.management.base import BaseCommand
from faker import Faker
from sector.models import Sector, Banner

class Command(BaseCommand):
    help = 'Preencher setores e banners com dados fictícios'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Criar diretório para armazenar imagens, se não existir
        if not os.path.exists('media/banners'):
            os.makedirs('media/banners')

        # Criar banners fictícios e armazenar em uma lista
        banners = []
        for _ in range(5):  # Criar 5 banners
            banner = Banner.objects.create(
                title=fake.catch_phrase(),
                description=fake.paragraph(),
            )
            self.create_fake_image(banner.title, is_banner=True)
            banners.append(banner)  # Adicionando o banner à lista
            self.stdout.write(self.style.SUCCESS(f'Banner "{banner.title}" criado.'))

        # Criar setores fictícios e associar banners
        for _ in range(10):  # Criar 10 setores
            sector = Sector.objects.create(
                name=fake.company(),
                description=fake.catch_phrase()
            )
            self.stdout.write(self.style.SUCCESS(f'Setor "{sector.name}" criado.'))

            # Associar todos os banners a este setor (ou escolha aleatoriamente)
            for banner in banners:
                sector.banners.add(banner)

            # Criar imagem fictícia para o setor
            self.create_fake_image(sector.name)

    def create_fake_image(self, name, is_banner=False):
        fake = Faker()
        
        # Criar uma imagem fictícia usando Pillow
        width, height = (1080, 1920) if is_banner else (1920, 1080)  # Tamanho 9:16 para banners
        image = Image.new('RGB', (width, height), color=(0, 0, 0))  # Cor de fundo preta
        image_path = f'media/banners/{name.replace(" ", "_")}.png'
        
        image.save(image_path)
        
        # Associar a imagem ao modelo
        if is_banner:
            banner = Banner.objects.get(title=name)
            with open(image_path, 'rb') as f:
                banner.image.save(f'{name}.png', File(f))
            banner.save()
        else:
            sector = Sector.objects.get(name=name)
            # Adicionando um banner aleatório ao setor (ajuste conforme necessário)
            # Aqui você pode adicionar uma lógica para escolher banners específicos, se preferir
            if sector.banners.exists():  # Verifica se o setor já tem banners
                sector.banners.add(sector.banners.first())  # Exemplo: adicionando um banner existente

        # Remover a imagem da pasta após salvar (opcional)
        os.remove(image_path)
