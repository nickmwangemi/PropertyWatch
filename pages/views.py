from django.shortcuts import render,redirect
from listings.models import Listing
from agents.models import Agent


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings,
    }
    return render(request,'pages/index.html',context)

def about(request):
    # Get all agents
    agents = Agent.objects.order_by('-hire_date')

    # Get MVP
    mvp_agents = Agent.objects.all().filter(is_mvp=True)

    context = {
        'agents':agents,
        'mvp_agents':mvp_agents,
    }
    
    return render(request,'pages/about.html',context)