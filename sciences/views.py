from django.shortcuts import render
from sciences.models import Science, Person

# Create your views here.
def science(request):
    return render(request, 'science.html',{})

def physics(request):
    physics = Person.objects.filter(science = 2)
    context = {'physics':physics}
    return render(request, 'physics.html',context)

def chemistry(request):
    chemistry = Person.objects.filter(science = 1)
    context = {'chemistry': chemistry}
    return render(request, 'chemistry.html',context)