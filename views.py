# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import RestaurantLocation

def restaurant_listview(request):
	template_name='restaurants/restaurants_list.html'
	queryset=RestaurantLocation.objects.all()
	context={
	     'object_list':queryset
	}

	return render(request,template_name,context)

