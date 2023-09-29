from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.forms import Movieform
from movieapp.models import Movies


# Create your views here.
def index(request):
    movie=Movies.objects.all()
    context={
        'movielist':movie
    }
    return render(request,"index.html",context)
def detail(request,movie_id):
    movie=Movies.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})

def addmovie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES.get('img')
        movie=Movies(name=name,desc=desc,year=year,img=img)
        movie.save();
        return redirect('/')
    return render(request,'add.html')

def delete(request,id):
    if request.method=='POST':
        movie=Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    movie=Movies.objects.get(id=id)
    form=Movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})