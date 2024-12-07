from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Item

def item_list(request):
    items = Item.objects.all()
    paginator = Paginator(items, 10)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'core/item_list.html', {'page_obj': page_obj})
