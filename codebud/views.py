from django.shortcuts import render,redirect
from .models import Room,Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def loginUser(request):
    page="login"
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method =="POST":
        username=request.POST.get('user_name').lower()
        password=request.POST.get('pass_word')

        try:
            user=User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "Username not found!")
        
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user) #creates a session in db and browser
            return redirect('/')
        else:
            messages.error(request, "Username or password does not exist!")

    context={
    "page":page
    }
    return render(request,"codebud/login_registration.html",context)

def registerUser(request):
    # page="register"

    form=UserCreationForm()

    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            # user=form.save()
            user=form.save(commit=False) #access user immediately after creation
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect("/")
        else:
            messages.error(request,"An error occured during registration")
    context={
        "form":form
    }
    return render(request,"codebud/login_registration.html",context)

#deletes token thus deletes user
def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
    
    # room=Room.objects.all()
    q=request.GET.get('q') if request.GET.get('q') is not None else ''
    # room=Room.objects.filter(topic__name__icontains=q)
    #search by three different parameters
    room=Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(id__icontains=q))
    
    rooms_found=room.count()
    topics=Topic.objects.all()[:8]
    context={
        "rooms":room,
        "topickey":topics,
        "rooms_found":rooms_found
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

@login_required(login_url="login")
def createRoom(request):
    form=RoomForm()
    print('EMPTY FORM CREATED!')

    if request.method =='POST':
        print('POST REQUEST RECEIVED!!')

        print('request method',request.method)

        form=RoomForm(request.POST)
        print('FORM POPULATED WITH POST DATA!!!',form)

        print(request.POST)
        if form.is_valid():
            print('FORM VALID,SAVING DATA!!!!')

            form.save()
            print('FORM DATA SAVED REDIRECTING YOU NOW!!!!!')

            return redirect("/")

    context={
        "form":form
    }
    return render(request,"codebud/roomform.html",context)

@login_required(login_url="login")
def updateRoom(request,pk):
    room_to_update=Room.objects.get(id=pk)
    form=RoomForm(instance=room_to_update)

    if request.user != room_to_update.host:
        return HttpResponse("Access denied for this page!")
    
    if request.method == "POST":
        form=RoomForm(request.POST,instance=room_to_update)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={
        "form":form
    }
    return render(request,"codebud/roomform.html",context)
'''
class TestPut():
    def get():
        pass
    def put():
        pass
    def post():
        pass
    def delete():
        pass
'''
#with DRF

@login_required(login_url="login")
def deleteRoom(request,pk):
    room_to_delete=Room.objects.get(id=pk)
    # print(room_to_delete)
    if request.user != room_to_delete.host:
        return HttpResponse("Access denied for this page!")
    
    if request.method == "POST":
        room_to_delete.delete()
        return redirect("/")
    context={
        "object":room_to_delete
    }
    return render(request,"codebud/deleteroom.html",context)