from django.http import JsonResponse
from .models import Sector

def sector_all(request):
    search = request.GET.get('search', '')
    sectors = Sector.objects.filter(name__icontains=search).values('id', 'name', 'description')
    
    return JsonResponse(list(sectors), safe=False)
