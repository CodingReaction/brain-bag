from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import DetailView, UpdateView, CreateView
from django.http import HttpResponseRedirect
from .models import Bag, Term
from .forms import BagForm, TermForm
import random

class CreateBagView(CreateView):
    model = Bag
    fields = ["name"]

    def get_success_url(self):
        return reverse("bags:index", kwargs={})


class CreateTermView(CreateView):
    model = Term
    fields = ["name", "url"]


class UpdateTermView(UpdateView):
    model = Term
    fields = ["name", "url"]

    def get_success_url(self):
        return reverse("bags:index", kwargs={})


def index(request):
    context = {"bags": Bag.objects.all()}
    return render(request, "bag_app/index.html", context=context)


def delete_term(request, id):
    term = get_object_or_404(Term, id=id)
    term.delete()

    return HttpResponseRedirect(reverse('bags'))