from sector.models import Sector


def global_vars(request):
    return {
        'site_name': 'SetorStyle',
        'sectors': Sector.objects.all()
    }
