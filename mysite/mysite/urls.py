from django.conf.urls import include, url
from django.contrib import admin
from tastypie.api import Api
from polls.api import QuestionResource, ChoiceResource
from events.api import CategoryResource, VenueResource, EventResource

from polls import views

question_resource = QuestionResource()
choice_resource = ChoiceResource()

category_resource = CategoryResource()
venue_resource = VenueResource()
event_resource = EventResource()

v1_api = Api(api_name='v1')
v1_api.register(QuestionResource())
v1_api.register(ChoiceResource())
v1_api.register(CategoryResource())
v1_api.register(VenueResource())
v1_api.register(EventResource())

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^events/', include('events.urls', namespace="events")),
    url(r'^question/', include('polls.urls')),
    url(r'^api/', include(question_resource.urls)),
    url(r'^api/', include(choice_resource.urls)),
    url(r'^api/', include(category_resource.urls)),
    url(r'^api/', include(venue_resource.urls)),
    url(r'^api/', include(event_resource.urls)),
    url(r'^api/', include(v1_api.urls)),
]
