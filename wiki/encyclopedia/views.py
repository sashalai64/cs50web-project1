from django.shortcuts import render
from . import util
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2 
from django.contrib import messages

class searchForm(forms.Form):
    q = forms.CharField(label='', widget=forms.TextInput(attrs={
      "class": "search",
      "placeholder": "Search Encyclopedia"}))

class createForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "New Page Title"
    }))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        "placeholder": "Enter Context"
    }))


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
    
    #if method not POST or not valid form, return to index page
    return HttpResponseRedirect(reverse('index'))


def new(request):
    #if GET (Initial Page Load), create an empty form
    if request.method == 'GET':
        return render(request, "encyclopedia/new.html", {
            "create_form": createForm()
        })

    #if POST (Form Submission), validate and render the form data submitted by the user
    elif request.method == 'POST':
        form = createForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
        else:
            messages.error(request, "Entry form not valid, please try again.")
            return render(request, "encyclopedia/new.html", {
                "create_form": form,
            })
            
        #if new entry already exists
        if util.get_entry(title):
            messages.error(request, "Entry already exists, please try again.")
            return render(request, "encyclopedia/new.html", {
                "create_form": form,
            })

        #if doesn't exist, save entry
        else:
            messages.success(request, f'Entry "{title}" created successfully.')
            util.save_entry(title, content)

            #take the user to the new entry page
            return HttpResponseRedirect(reverse('entry', args=(title, )))