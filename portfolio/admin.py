from django.contrib import admin
from adminsortable.admin import SortableAdmin, SortableStackedInline
from .models import (
    Service, PortfolioItem, TeamMember, SocialLink, Client)


class ServiceAdmin(SortableAdmin):
    model = Service


class PortfolioItemAdmin(SortableAdmin):
    model = PortfolioItem


class SocialLinkInline(SortableStackedInline):
    model = SocialLink


class TeamMemberAdmin(SortableAdmin):
    model = TeamMember
    inlines = [SocialLinkInline]


class ClientAdmin(SortableAdmin):
    model = Client

admin.site.register(Service, ServiceAdmin)
admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Client, ClientAdmin)
