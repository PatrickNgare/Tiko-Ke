from django.shortcuts import render
from . models import Profile,EventType,Event



def index(request):
    
    events= Event.objects.all()
    print(events)

    return render(request,'temps/index.html',{"events": events})
