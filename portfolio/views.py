from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

class PortfolioView(TemplateView):
	template_name = "portfolio/index.html"
