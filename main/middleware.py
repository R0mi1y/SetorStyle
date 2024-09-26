from django.shortcuts import render
from django.template.loader import render_to_string

class InnerHTMLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return self.process_template_response(request, response)

    def process_template_response(self, request, response):
        if not request.GET.get('inner_html') == 'true':
            print('not inner_html')
            template_name = response.template_name if hasattr(response, 'template_name') else '_base.html'
            context = response.context_data if hasattr(response, 'context_data') else {}
            response.content = render_to_string(template_name, context)
        
        return response
