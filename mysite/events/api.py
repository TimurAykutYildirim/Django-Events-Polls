from tastypie.resources import ModelResource
from tastypie import fields
from events.models import Category, Venue, Event
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'

class VenueResource(ModelResource):
    class Meta:
        queryset = Venue.objects.all()
        resource_name = 'venue'

class EventResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category')
    venue = fields.ForeignKey(VenueResource, 'venue')
    class Meta:
        filtering = {
            'category': ALL_WITH_RELATIONS,
            'venue': ALL_WITH_RELATIONS,
        }
        queryset = Event.objects.all()
        resource_name = 'event'


# DISARIDAN FK ALMASAYDI BOYLE OLURDU
