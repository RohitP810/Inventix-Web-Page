from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'Home.html')
def gallery(request):
    return render(request, 'Gallery.html')
def event(request):
    return render(request, 'eventsfrontpg.html')
def upcoming(request):
    return render(request, 'upcoming.html')
def completed(request):
    return render(request, 'completed.html')
def form(request):
    return render(request, 'form.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')