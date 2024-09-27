from django.shortcuts import redirect, render
from django.urls import reverse

from SetorStyle.utils import redirect_inner_html
from sector.forms import BannerForm, SectorForm
from sector.models import Banner, Sector

def detail_sector(request, id):
    sector = Sector.objects.filter(id=id).first()
    form_sector = SectorForm(instance=sector)
        
    return render(request, 'pages/home.html', {'sector': sector, 'form_banners': [BannerForm(instance=i) for i in sector.banners.all()], 'form_sector': form_sector})


def create_or_edit_sector(request, id=None):
    sector = None
    
    if id:
        sector = Sector.objects.filter(id=id).first()
        form_sector = SectorForm(instance=sector)
        
    if request.method == 'POST':
        
        form_sector = SectorForm(request.POST, instance=sector)
        if form_sector.is_valid():
            form_sector.save()
            
            sector = form_sector.instance
    else:
        form_sector = SectorForm(instance=sector)
    
    return render(request, 'pages/home.html', {
            'sector': sector, 
            'form_banners': [BannerForm(instance=i) for i in sector.banners.all()], 
            'form_sector': form_sector
        })


def create_or_edit_banner(request, id=None):
    id_sector = request.POST.get('sector')
    sector = Sector.objects.filter(id=id_sector).first()

    if not sector:
        return redirect_inner_html('home')

    banner_instance = Banner.objects.filter(id=id).first() if id else None

    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=banner_instance)
        
        if form.is_valid():
            banner = form.save()

            if not banner_instance:
                sector.banners.add(banner)
    else:
        form = BannerForm(instance=banner_instance)

    return render(request, 'pages/home.html', {
        'sector': sector,
        'form_banners': [BannerForm(instance=i) for i in sector.banners.all()],
        'form_sector': SectorForm(instance=sector),
        'form_banner': form,
    })


def delete_sector(request, id):

    element = Sector.objects.filter(id=id).first()
    
    if element:
        element.delete()
        
    return redirect_inner_html('home')
    

def delete_banner(request, id):
    element = Banner.objects.filter(id=id).first()
    sector = element.sector_set.first()
    
    if element:
        element.delete()
        
    return render(request, 'pages/home.html', {
        'sector': sector,
        'form_banners': [BannerForm(instance=i) for i in sector.banners.all()],
        'form_sector': SectorForm(instance=sector),
    })


def get_presentation_banner(request, id):
    banner = Banner.objects.filter(id=id).first()
    
    return banner.get_presentation()