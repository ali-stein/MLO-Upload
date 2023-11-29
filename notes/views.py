
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Notes
from django.views.generic import DetailView, DeleteView, UpdateView, ListView, CreateView
from . forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()
        

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = 'note'
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/notes'
    form_class = NotesForm
    login_url = "/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = '/notes'
    form_class = NotesForm
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/notes'
    template_name = "notes/notes_delete.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()
    
