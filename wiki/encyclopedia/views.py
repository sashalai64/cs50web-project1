from django.shortcuts import render
from . import util
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2 

class searchForm(forms.Form):
    q = forms.CharField(label='', widget=forms.TextInput(attrs={
      "class": "search",
      "placeholder": "Search Encyclopedia"}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "search_form": searchForm()
    })

def entry(request, title):
    content = util.get_entry(title)

    if content != None:
        #convert text to HTML
        markdown_text = markdown2.markdown(content)

        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": markdown_text,
            "search_form": searchForm()
        })
    
    related = util.get_related(title)

    return render(request, "encyclopedia/error.html", {
        "title": title,
        "related_entries": related,
        "search_form": searchForm()
    })


def search(request):
    if request.method == 'POST':
        form = searchForm(request.POST)

        #if the form is valid, try to match with the entries
        if form.is_valid():
            query = form.cleaned_data['q']
            match = util.get_entry(query)

            print('search request:', query)

            #if query is matched
            if match:
                return HttpResponseRedirect(reverse('entry', args=(query,)))

            #display related results
            related = util.get_related(query)            

            return render(request, "encyclopedia/search.html", {
                "query": query,
                "related_entries": related,
                "search_form": searchForm()
            })
    
    #if method not POST or not valid form, return to indxe page
    return HttpResponseRedirect(reverse('index'))