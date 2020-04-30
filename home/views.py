from django.shortcuts import render
from property.models import Property, Category
from .models import HomeModel
from agents.models import Agent
from django.db.models import Count
# Create your views here.
def home(request):
	category_list = Category.objects.all()
	# category_list = Category.objects.annotate(property_count=Count('property')).values('category_name', 'property_count', 'image')
	# print(category_list)
	property_lists = Property.objects.all()
	home_list = HomeModel.objects.all()
	agent_list = Agent.objects.all()
	template = 'home/home.html'
	context = {
		'category_list_home': category_list,
		'property_lists_home': property_lists,
		'home_list': home_list,
		'agent_list_home': agent_list,
	}

	return render(request, template, context)