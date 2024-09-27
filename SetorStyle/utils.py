from django.shortcuts import redirect
from django.urls import reverse

def redirect_inner_html(name, **kwargs):
    url = reverse(name, kwargs=kwargs)  # Corrigido kwargs para ser passado explicitamente
    url += '?inner_html=true'
    
    return redirect(url)