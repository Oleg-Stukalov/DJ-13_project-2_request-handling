import csv

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    #file = settings.BUS_STATION_CSV
    with open(settings.BUS_STATION_CSV, newline='') as file:
        data = csv.DictReader(file)
    decoded_file = file.read().decode('cp1251').splitlines()
    data = csv.DictReader(decoded_file)

    for row in data:
        print(row['Name'], row['Street'], row['District'])
    return HttpResponse(row)

    #################
    current_page = 1
    next_page_url = 'write your url'
    return render_to_response('index.html', context={
        'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'}],
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })


# def articles_view(request):
#     paginator = Paginator(all_articles, 2)
#     current_page = request.GET.get('page', 1)
#     articles = paginator.get_page(current_page)
#     prev_page, next_page = None, None
#     if articles.has_previous():
#         prev_page = articles.previous_page_number
#     if articles.has_next():
#         next_page = articles.next_page_number
#     context = {
#         'articles': articles,
#         'prev_page': prev_page,
#         'next_page': next_page,
#         'current_page': articles.number
#     }
#     return render(request, 'demo/articles.html',
#               context=context)
