from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Student
from django.views.generic import (CreateView, ListView,
                                    UpdateView, DeleteView)

# Create your views here.

class StudentListView(ListView):
    model = Student
    template_name = 'index.html'

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('list')