from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns(
    'portfolio.views',
    url(r'^privacy/(?P<slug>.*)/$', PrivacyView.as_view(), name='privacy'),
    url(r'^$', PortfolioView.as_view(), name='portfolio'),
)
