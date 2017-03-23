from django.shortcuts import render, HttpResponseRedirect
from .models import Treasure
from .forms import TreasureForm

def index(request):
    treaures = Treasure.objects.all()
    form = TreasureForm()
    return render(request,'index.html',{'treaures':treaures, 'form':form})


def detail(request, tre_id):
    treaures = Treasure.objects.get(id=tre_id)
    return render(request,'detail.html',{'treaures':treaures})

def post_treasure(request):
    form = TreasureForm(request.POST)
    if form.is_valid():
        treasure = Treasure(name = form.cleaned_data['name'],
                            value = form.cleaned_data['value'],
                            material = form.cleaned_data['material'],
                            location = form.cleaned_data['location'],
                            img_url = form.cleaned_data['img_url'],
                           )
        treasure.save()
    return HttpResponseRedirect('/')




"""
link1 = "https://s-media-cache-ak0.pinimg.com/236x/4b/87/f4/4b87f4ed46a5d3edba956643915af524.jpg"
link2 = "https://s-media-cache-ak0.pinimg.com/236x/2e/c2/8d/2ec28d7f99c69b8f509f72122f072df6.jpg"
link3 = "https://s-media-cache-ak0.pinimg.com/236x/fc/b5/1c/fcb51cf6a50696b10b4b2014324b0126.jpg"
"""
