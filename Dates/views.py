import datetime

from django.shortcuts import render

from Dates.models import Event


def get_events(request):
    events = Event.objects.filter(date__gte=datetime.date.today()).order_by('date')

    context = {
        'events': events[:5]
    }
    return render(request, 'event/show_events.html', context)
