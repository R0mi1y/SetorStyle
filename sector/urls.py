from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path('add/', create_or_edit_sector, name='add_sector'),
    path('add/banner/', create_or_edit_banner, name='add_banner'),
    
    path('update/<int:id>/', create_or_edit_sector, name='update_sector'),
    path('update/banner/<int:id>/', create_or_edit_banner, name='update_banner'),
    
    path('delete/<int:id>/', delete_sector, name='delete_sector'),
    path('delete/banner/<int:id>/', delete_banner, name='delete_banner'),
    
    path('<int:id>/', detail_sector, name='details_sector'),
    path('banner/preview/<int:id>/', get_presentation_banner, name='get_presentation_banner_preview'),
    
    # API
    path('api/all/', sector_all, name='get_all_sectors'),
]
