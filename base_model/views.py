from django.views.generic import TemplateView, RedirectView


class HomeView(TemplateView):
    template_name = 'index.html'


class Error404(TemplateView):
    template_name = '404_error.html'
