from django.shortcuts import render
from django.views import View


class MainView(View):

    def get(self, request):
        return render(request, 'MainView/index.html')


class DepartureView(View):

    def get(self, request):
        return render(request, 'DepartureView/departure.html')


class TourView(View):

    def get(self, request):
        return render(request, 'TourView/tour.html')
