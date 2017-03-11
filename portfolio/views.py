from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView
from .models import Service, PortfolioItem, TeamMember, Client, PrivacyPolicy


class PortfolioView(TemplateView):
    template_name = "portfolio/index.html"

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        context["portfolio_items"] = PortfolioItem.objects.all()
        context["team_members"] = TeamMember.objects.all()
        context["clients"] = Client.objects.all()
        return context


class PrivacyView(DetailView):
    model = PrivacyPolicy
