from django.shortcuts import render
from . models import Profile,EventType,Event



def index(request):
    
    events= Event.objects.all()
    
    return render(request,'temps/index.html',{"events": events})


def description(request,id):


    single=Event.objects.get(id=id)

    print(single)



    return render(request ,'temps/descritpion.html',{"single":single})