from django.urls import path
from .views import AboutPage, RulesPage

app_name = 'pages'

urlpatterns = [
    path('about/', AboutPage.as_view(), name='about'),
    path('rules/', RulesPage.as_view(), name='rules'),
]
