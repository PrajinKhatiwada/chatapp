from django.shortcuts import render

# chatapp views

def home(request):
    return render(request,'home.html')



def room(request):
    return render(request,'room.html')