from django.shortcuts import render, redirect
import calendar 
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, EventLocation
from .forms import EventLocationForm, EventForm


# Delete a location
def delete_location(request, location_id):
    location = EventLocation.objects.get(pk=location_id)
    location.delete()
    return redirect('list-eventlocations')

# Delete an event
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request, 'events/update_event.html', 
                  {'event': event,
                   'form': form,})

def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/calendar/add_event/?submitted=True')
         
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})

def update_location(request, location_id):
    location = EventLocation.objects.get(pk=location_id)
    form = EventLocationForm(request.POST or None, instance=location)
    if form.is_valid():
        form.save()
        return redirect('list-eventlocations')
    return render(request, 'events/update_location.html', 
                  {'location': location,
                   'form': form,})

def show_location(request, location_id):
    location = EventLocation.objects.get(pk=location_id)
    return render(request, 'events/show_location.html', 
                  {'location': location})

def list_eventlocations(request):
    location_list = EventLocation.objects.all()
    return render(request, 'events/locations.html', 
                  {'location_list': location_list})

def add_eventlocation(request):
    submitted = False
    if request.method == "POST":
        form = EventLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/calendar/add_eventlocation/?submitted=True')
         
    
         
    else:
        form = EventLocationForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'events/add_eventlocation.html', {'form': form, 'submitted': submitted})
     

def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', 
                  {'event_list': event_list})

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "World"
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    


# Create a calendar 
    cal = HTMLCalendar().formatmonth(year, month_number)

    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M %p')
    return render(request, 
        'events/home.html', {
        "name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time": time,
    })
