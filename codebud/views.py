from django.shortcuts import render,redirect
from .models import Room
from .forms import RoomForm


# Create your views here.
def home(request):
    room=Room.objects.all()
    context={
        "rooms":room
    }
    return render(request,"codebud/home.html",context)

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

def createRoom(request):
    form=RoomForm()

    if request.method =='POST':
        form=RoomForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context={
        "form":form
    }
    return render(request,"codebud/roomform.html",context)

def updateRoom(request,pk):
    room_to_update=Room.objects.get(id=pk)
    form=RoomForm(instance=room_to_update)
    if request.method == "POST":
        form=RoomForm(request.POST,instance=room_to_update)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={
        "form":form
    }
    return render(request,"codebud/roomform.html",context)

def deleteRoom(request,pk):
    room_to_delete=Room.objects.get(id=pk)
    # print(room_to_delete)
    if request.method == "POST":
        room_to_delete.delete()
        return redirect("/")
    context={
        "object":room_to_delete
    }
    return render(request,"codebud/deleteroom.html",context)