from django.shortcuts import render, redirect
from .models import Event
from django.utils import timezone
from django.http import HttpResponse

def add_event(request, event_type):
    # Determine the event type
    if event_type not in ['sleep', 'feed', 'poop', 'diaper_change']:
        return HttpResponse("Invalid event type.", status=400)
    
    # Record the event
    event = Event.objects.create(event_type=event_type, event_time=timezone.now())
    
    return redirect('event_list')

def event_list(request):
    events = Event.objects.all().order_by('-event_time')
    return render(request, 'monitor/event_list.html', {'events': events})
