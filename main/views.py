from django.shortcuts import render, HttpResponse
from .models import ToDo
from .models import ToMeet

# Create your views here.
def homepage(request):
    return render(request, "index.html")
def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})
def meeting(request):
    tomeet_list = ToMeet.objects.all()
    return render(request, "meeting.html", {"tomeet_list": tomeet_list})