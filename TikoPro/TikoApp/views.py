from django.shortcuts import render
from . models import Profile,EventType,Event
from django.contrib.auth.decorators import login_required




def index(request):
    
    events= Event.objects.all()
    
    return render(request,'temps/index.html',{"events": events})


@login_required(login_url='/accounts/login/')
def description(request,id):


    single=Event.objects.get(id=id)

    print(single)



    return render(request ,'temps/descritpion.html',{"single":single})