from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import PortfolioItem, TeamMember

class PortfolioView(TemplateView):
	template_name = "portfolio/index.html"

	def get_context_data(self, **kwargs):
		context = super(PortfolioView, self).get_context_data(**kwargs)
		context["portfolio_items"] = PortfolioItem.objects.all()
		context["team_members"] = TeamMember.objects.all()
		return context
