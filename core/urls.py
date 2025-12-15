from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('contacts/', views.ContactListView.as_view(), name='contact_list'),
    path('contacts/new', views.ContactCreateView.as_view(), name='contact_create'),
    path('contacts/int:pk/edit/', views.ContactUpdateView.as_view(), name='contact_update'),
    path('contacts/int:pk/delete/', views.ContactDeleteView.as_view(), name='contact_delete'),

    path('Events/', views.EventListView.as_view(), name='event_list'),
    path('Events/new', views.EventCreateView.as_view(), name='event_create'),
    path('Events/int:pk/edit/', views.EventUpdateView.as_view(), name='event_update'),
    path('Events/int:pk/delete/', views.EventDeleteView.as_view(), name='event_delete'),
]
