from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse
from django.template import loader

from .models import Event, Venue, Category

"""
class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'latest_events'

    def get_queryset(self):
        #Return last 5 events.
        return Event.object.order_by('starts')[:5]
"""

def index(request):
    values = dict()
    events = Event.objects.all()
    values['events'] = events
    return render_to_response('events/index.html', values)