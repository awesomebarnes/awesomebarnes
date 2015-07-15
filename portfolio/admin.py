from django.contrib import admin
from adminsortable.admin import SortableAdmin
from .models import PortfolioItem, TeamMember, SocialLink


class PortfolioItemAdmin(SortableAdmin):
    model = PortfolioItem


class TeamMemberAdmin(SortableAdmin):
    model = TeamMember


class SocialLinkAdmin(SortableAdmin):
    model = SocialLink

admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)
