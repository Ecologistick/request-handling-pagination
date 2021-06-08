from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination.app.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    Sergey = []
    with open(BUS_STATION_CSV, newline='', encoding="cp1251") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            a = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
            Sergey.append(a)
    paginator = Paginator(Sergey, 2)
    current_page = request.GET.get('page')
    articles = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if articles.has_previous():
        prev_page = articles.previous_page_number
    if articles.has_next():
        next_page = articles.next_page_number
    return render(request, 'index.html', context={
        'bus_stations': Sergey,
        # 'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'},
        #                  {'Name': 'другое название', 'Street': 'другая улица', 'District': 'другой район'}],
        'current_page': articles.number,
        'prev_page_url': None,
        'next_page_url': next_page,
    })
