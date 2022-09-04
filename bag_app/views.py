from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import DetailView, UpdateView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Bag, Term
from .forms import AutofillBagForm 
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import requests
import random
from math import floor

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
    bags = Bag.objects.all()
    columns_count = 3
    bags_per_col = floor(len(bags) / columns_count)
    context = {"bags_columns": [bags[: bags_per_col], bags[bags_per_col: bags_per_col* 2], bags[bags_per_col*2 :  ]]}
    return render(request, "bag_app/index.html", context=context)


def delete_term(request, id):
    term = get_object_or_404(Term, id=id)
    term.delete()

    return HttpResponseRedirect(reverse('bags'))



def autofill_bag_from_url(request):
    if request.method == 'POST':
        form = AutofillBagForm(request.POST)
        if form.is_valid():
            target_url = form.cleaned_data['url']
            html_to_scrape = requests.get(target_url)
            html_to_scrape = html_to_scrape.text
            parent_selector = form.cleaned_data['parent_selector']
            children_selector = form.cleaned_data['children_selector']
            soup = BeautifulSoup(html_to_scrape, 'html.parser')
            print('--------------- SCRAPING START ---------------')
            scrapping_results = soup.select(f'{parent_selector} {children_selector}')
            new_bag = Bag.objects.create(name=f"(auto) {target_url[:25]}")
            for link in scrapping_results:
                term_link = link.get('href')
                if not bool(urlparse(term_link).netloc):
                    term_link = urljoin(target_url, term_link)
                new_bag.term_set.create(name=link.get_text(strip=True), url=term_link)
            return HttpResponseRedirect(reverse('bags:index', kwargs={}))
    else:
        form = AutofillBagForm()

    return render(request, 'bag_app/autofill_bag_form.html', {'form': form})