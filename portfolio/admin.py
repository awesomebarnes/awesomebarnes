from django.contrib import admin
from adminsortable.admin import SortableAdmin
from .models import (
    Service, PortfolioItem, TeamMember, SocialLink, Client)


class ServiceAdmin(SortableAdmin):
    model = Service


class PortfolioItemAdmin(SortableAdmin):
    model = PortfolioItem


class TeamMemberAdmin(SortableAdmin):
    model = TeamMember


class SocialLinkAdmin(SortableAdmin):
    model = SocialLink


class ClientAdmin(SortableAdmin):
    model = Client

admin.site.register(Service, ServiceAdmin)
admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)
admin.site.register(Client, ClientAdmin)
