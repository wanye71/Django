from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView

from .models import Notes

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url = '/smart/notes'

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes_list"
    template_name = "notes/notes_list.html"
    
class NotesDetailView(DetailView):
    model = Notes 
    context_object_name = "note_details"
    template_name = "notes/notes_detail.html"