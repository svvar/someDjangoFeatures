from datetime import datetime
from django.db.models import Q
from django.shortcuts import render

from museum.models import Product

def index(request):
    return render(request, 'index.html')
def tickets(request):
    date = request.GET.get('daterange')
    minQ = request.GET.get('minQ')
    maxQ = request.GET.get('maxQ')

    if (date, minQ, maxQ) == (None, None, None):
        products = Product.objects.all()[:1000]
        return render(request, 'tickets.html', context={'products': products})

    filter_query = Q()

    if date:
        start_date = datetime.strptime(date.split(' - ')[0], '%d/%m/%Y').strftime('%Y-%m-%d')
        end_date = datetime.strptime(date.split(' - ')[1], '%d/%m/%Y').strftime('%Y-%m-%d')
        filter_query &= Q(date_added__range=[start_date, end_date])
    if minQ and maxQ:
        filter_query &= Q(quantity__range=[minQ, maxQ])
    elif maxQ:
        filter_query &= Q(quantity__lte=maxQ)
    elif minQ:
        filter_query &= Q(quantity__gte=minQ)

    products = Product.objects.filter(filter_query)
    fields_input = {'date1': date.split(' - ')[0], "date2": date.split(' - ')[1], 'minQ': minQ, 'maxQ': maxQ}
    return render(request, 'tickets.html', context={'products': products} | fields_input)
