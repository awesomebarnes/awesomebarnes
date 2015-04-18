from django.conf.urls import patterns, url

urlpatterns = patterns('portfolio.views',
	url(r'^$', PortfolioView.as_view(), name='portfolio'),
)
