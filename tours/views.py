from django.shortcuts import render
from django.views import View
from django.http import Http404
from django.http import HttpResponseNotFound, HttpResponseServerError
from tours.information import tours, departures, title, subtitle, description
from random import shuffle


def custom_handler404(request, exception):
    return HttpResponseNotFound("Страница не найдена!")


def custom_handler500(request):
    return HttpResponseServerError("Server error!")


class MainView(View):

    def get(self, request, *args, **kwargs):
        keys = list(tours.keys())[:6]
        shuffle(keys)
        shuffledTours = dict()
        for key in keys:
            shuffledTours.update({key: tours[key]})

        return render(request, 'index.html', {"tours": shuffledTours, "departures": departures, "title": title,
                                              "subtitle": subtitle, "description": description})


class DepartureView(View):

    def get(self, request, departure, *args, **kwargs):
        if departure not in departures:
            raise Http404

        count_tours = 0
        min_price = 10 ** 10
        max_price = 0
        min_nights = 10 ** 10
        max_nights = 0
        for tour in tours.values():
            if tour["departure"] == departure:
                count_tours += 1
                if tour["price"] < min_price:
                    min_price = tour["price"]
                if tour["price"] > max_price:
                    max_price = tour["price"]
                if tour["nights"] < min_nights:
                    min_nights = tour["nights"]
                if tour["nights"] > max_nights:
                    max_nights = tour["nights"]

        return render(request, 'departure.html',
                      {"departures": departures, "title": title,
                       "min_price": min_price, "max_price": max_price,
                       "min_nights": min_nights, "max_nights": max_nights,
                       "city": departures[departure], "count_tours": count_tours,
                       "tours": tours, "departure": departure}
                      )


class TourView(View):

    def get(self, request, id, *args, **kwargs):
        if id not in tours.keys():
            raise Http404

        return render(request, 'tour.html',
                      {'tour': tours[id], "city": departures[tours[id]["departure"]],
                       'departures': departures})
