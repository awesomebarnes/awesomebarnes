from django.db.models import (
    CharField, TextField, ForeignKey, URLField)
from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey
from autoslug import AutoSlugField
from filer.fields.image import FilerImageField


class Service(Sortable):
    slug = AutoSlugField(populate_from='name')
    name = CharField(max_length=50, blank=False, null=False)
    description = TextField(max_length=1000, blank=True, null=True)
    icon = CharField(max_length=100, blank=False, null=False,
                     default="fontawesome-desktop")

    class Meta(Sortable.Meta):
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()


class PortfolioItem(Sortable):
    slug = AutoSlugField(populate_from='name')
    name = CharField(max_length=50, blank=False, null=False)
    caption = CharField(max_length=100, blank=True, null=True)
    headline = CharField(max_length=250, blank=True, null=True)
    image = FilerImageField(null=True, blank=True)
    description = TextField(max_length=1000, blank=True, null=True)

    class Meta(Sortable.Meta):
        verbose_name = "Portfolio item"
        verbose_name_plural = "Portfolio items"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()


class TeamMember(Sortable):
    slug = AutoSlugField(populate_from='name')
    name = CharField(max_length=50, blank=False, null=False)
    caption = CharField(max_length=250, blank=True, null=True)
    image = FilerImageField(null=True, blank=True)
    description = TextField(max_length=1000, blank=True, null=True)

    class Meta(Sortable.Meta):
        verbose_name = "Team member"
        verbose_name_plural = "Team members"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()


class SocialLink(Sortable):
    slug = AutoSlugField(populate_from='name', unique_with='team_member')
    name = CharField(max_length=50, blank=False, null=False)
    team_member = SortableForeignKey('TeamMember', blank=False, null=False)
    url = URLField(max_length=250, blank=False, null=False)
    icon_class = CharField(max_length=100, blank=False, null=False,
                           default="fontawesome-at")

    class Meta(Sortable.Meta):
        verbose_name = "Social link"
        verbose_name_plural = "Social links"

    def __str__(self):
        if self.team_member:
            return self.team_member.name + ": " + self.name
        return self.name

    def __unicode__(self):
        return self.__str__()


class Client(Sortable):
    slug = AutoSlugField(populate_from='name')
    name = CharField(max_length=50, blank=False, null=False)
    url = URLField(max_length=250, blank=True, null=True)
    image = FilerImageField(null=True, blank=True)

    class Meta(Sortable.Meta):
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()
