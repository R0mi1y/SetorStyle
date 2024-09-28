from django.shortcuts import render
from django.template.loader import render_to_string

from SetorStyle import settings

class InnerHTMLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return self.process_template_response(request, response)

    def process_template_response(self, request, response):
        if request.path.startswith(settings.STATIC_URL) or request.path.startswith(settings.MEDIA_URL):
            return response
        
        if request.path.startswith('/sector/banner/'):
            return response
        
        elif request.method == 'GET' and not request.GET.get('inner_html') == 'true':
            template_name = response.template_name if hasattr(response, 'template_name') else '_base.html'
            context = response.context_data if hasattr(response, 'context_data') else {}
            response.content = render_to_string(template_name, context)
        
        return response
