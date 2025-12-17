from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Contact, Event
from .forms import ContactForm, EventForm
from django.utils import timezone
from django.db.models import Q

class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        queryset = Contact.objects.all()
        q= self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(full_name__icontains=q) |
                Q(organisation__icontains=q)
            )
        return queryset

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'form.html'
    success_url = reverse_lazy('contact_list')

class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'form.html'
    success_url = reverse_lazy('contact_list')

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('contact_list')

class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'form.html'
    success_url = reverse_lazy('event_list')

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'form.html'
    success_url = reverse_lazy('event_list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('event_list')

class HomePageView(ListView):
    model = Event
    template_name = 'home.html'
    context_object_name = 'today_events'

    def get_queryset(self):
        now = timezone.now()
        start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        end = now.replace(hour=23, minute=59, second=59, microsecond=999999)
        return Event.objects.filter(datetime__range=(start, end)).order_by('datetime')

