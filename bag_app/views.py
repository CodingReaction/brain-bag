from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Bag, Term
from .forms import BagForm, TermForm
import random

def create_bag(request):
    if request.method == "POST":
        form = BagForm(request.POST)
        if form.is_valid():
            new_bag_name = form.cleaned_data["bag_name"]
            if Bag.objects.filter(name=new_bag_name).count() == 0:
                new_bag = Bag(name=new_bag_name)
                new_bag.save()
            return HttpResponseRedirect(reverse("bags"))
    else:
        form = BagForm()
    
    return render(request, 'bag_app/new_bag.html', {"form": form})


def create_term(request):
    if request.method == "POST":
        form = TermForm(request.POST)
        #bag_id = request.POST.get("bag_id")
        if form.is_valid():
            new_term = Term(bag=form.cleaned_data["term_bag"], name=form.cleaned_data["term_name"], url=form.cleaned_data["term_url"])
            new_term.save()
        return HttpResponseRedirect(reverse("bags"))
    else:
        form = TermForm()

    return render(request, 'bag_app/new_term.html', {"form": form})

CIRCLE_RADIUS = 150
def index(request):
    context = {"bags": Bag.objects.all(), "term_coords":{}}
    for bag in context["bags"]:
        for term in bag.term_set.all():
            left = random.randint(-CIRCLE_RADIUS, CIRCLE_RADIUS) 
            top = random.randint(-CIRCLE_RADIUS, CIRCLE_RADIUS) 
            while left ** 2 + top ** 2 > CIRCLE_RADIUS ** 2:
                left = random.randint(-CIRCLE_RADIUS, CIRCLE_RADIUS) 
                top = random.randint(-CIRCLE_RADIUS, CIRCLE_RADIUS) 

            context["term_coords"][term.id] = f"left: { 200 + left}px; top: { 200 + top}px"
    return render(request, "bag_app/index.html", context=context)