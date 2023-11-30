from .models import *
def menu_links(request):
    links = Category.objects.all()
    return {'links':links}
def subcat_links(request):
    sublinks = Subcategory.objects.all()
    return {'sublinks':sublinks}