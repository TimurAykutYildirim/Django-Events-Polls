from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    """Different types of events like cinema, cinema for kids, theatre, etc.
        picture is an image that can be used for an event if there is no image
        for the event itself"""
    name = models.CharField(u"Name", max_length=50)
    # picture = ResizedImageField(upload_to=upload_to_category, max_width=185, max_height=185, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = u"Category"
        verbose_name_plural = u"Categories"
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Venue(models.Model):
    """Describes the venues, Opening hours, location, etc."""
    name = models.CharField(u"Name", max_length=50)
    opening_hours = models.TextField(u"Opening")
    address = models.TextField(u"Address")
    description = models.TextField(u"Description")
    # description = MarkdownTextField(u"Description")
    # we resize uploaded pics th 185px, because the will used as thumb on the web.
    # picture = ResizedImageField(upload_to=upload_to_venue, max_width=185, max_height=185)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = u"Venue"
        verbose_name_plural = u"Venues"
        ordering = ['name']

    def __unicode__(self):
        return self.name

"""Any event that does'nt span over various days. comments is used for internal comments that are not meant for publication"""
class Event(models.Model):
    title = models.CharField(u"Title", max_length=50)
    # description = MarkdownTextField(u"Description")
    description = models.TextField(u"Description")
    comments = models.TextField(u"Comments")
    date = models.DateField()
    starts = models.TimeField(blank=True, null=True)
    ends = models.TimeField(blank=True, null=True)
    price = models.CharField(default="Free Entrance", max_length=50)
    venue = models.ForeignKey(Venue)
    category = models.ForeignKey(Category)
    # picture = ResizedImageField(upload_to=upload_to_event, max_width=185, max_height=185, blank=True, null=True)

    status = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = u"Event"
        verbose_name_plural = u"Events"
        ordering = ['date', 'starts']

    def __unicode__(self):
        return self.title