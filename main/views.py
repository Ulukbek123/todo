from django.shortcuts import render, HttpResponse, redirect
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
def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)
def add_tomeet(request):
    form = request.POST
    text = form["tomeet_text"]
    tomeet = ToMeet(name=text)
    tomeet.save()
    return redirect(meeting)