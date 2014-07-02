from django.views import generic
from .models import *



class CategoryIndexView(generic.ListView):
    model = Category
    #template_name = ''
    queryset = Category.objects.filter(parent=None)
    paginate_by = 20

    
    
class CategoryDetailView(generic.DetailView):
    model = Category

