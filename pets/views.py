from django.shortcuts import HttpResponse
from django.template import loader
from .models import Pet

def index(request):
    return HttpResponse("Pets response")

def pets_list(request):
    pets = Pet.objects.all().values()
    template = loader.get_template('pets.html')
    context = {
        'pets': pets,
        }
    return HttpResponse(template.render(context, request))