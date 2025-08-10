from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "core/home.html"
   
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title'] = "My Home Page Playground"
        context['message'] = "Welcome to the Home Page!"
        return render(request, self.template_name, context)


class SamplePageView(TemplateView):
    template_name = "core/sample.html"