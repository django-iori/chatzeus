from django.views import generic
from django.http import HttpResponse

# Create your views here.
class IndexViews(generic.TemplateView):
    template_name = "chat/index.html"