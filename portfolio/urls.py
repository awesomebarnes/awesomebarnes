from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('portfolio.views',
	url(r'^$', PortfolioView.as_view(), name='portfolio'),
)
