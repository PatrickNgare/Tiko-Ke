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


def search(request):
    
    if 'event' in request.GET and request.GET["event"]:
        search_term = request.GET.get("event")
        searched_event = Event.search_event(search_term)
        message = f"{search_term}"
        

        return render(request, 'temps/search.html',{"message":message,"searched_event": searched_event})

    else:
        message = "You haven't searched for any term"
        return render(request, 'temps/search.html',{"message":message})    