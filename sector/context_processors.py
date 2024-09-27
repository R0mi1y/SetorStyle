from .models import Sector
from .forms import SectorForm, BannerForm

def global_vars(request):
    return {
        'site_name': 'SetorStyle',
        'sectors': Sector.objects.all(),
        'form_sector': SectorForm(),
        'form_banner': BannerForm(),
    }
