from django.contrib import admin
from adminsortable.admin import SortableAdmin
from .models import PortfolioItem

class PortfolioItemAdmin(SortableAdmin):
    model = PortfolioItem

admin.site.register(PortfolioItem, PortfolioItemAdmin)
