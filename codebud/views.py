from django.shortcuts import render
from .models import Room


# Create your views here.

# rooms=[
#     {'id':1,'name':'Java'},
#    {'id':2,'name':'sql'},
#    {'id':3,'name':'django'},
#    {'id':4,'name':'flask'},
# ]
def home(request):
    room=Room.objects.all()
    context={
        "rooms":room
    }
    return render(request,"codebud/home.html",context)

# def room(request):
#     return render(request,"codebud/room.html")

def oneroom(request,pk):
    # room=None
    # for item in rooms:
    #     if item['id'] ==int(pk):
    #         room=item
    # context={
    #     "roomey":room
    # }
    room=Room.objects.get(id=pk)
    context={
        "roomey":room
    }
    return render(request,"codebud/room.html",context)