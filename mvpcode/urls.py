from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    path('articles/', ArticlesView.as_view(), name='articles'),
    path('articles/<slug:slug>', ArticlesDetail.as_view(), name='articledetail'),

    path('cources/', CourcesPageView.as_view(), name='cources'),

    path('contacts/', ContactPageView.as_view(), name='contacts')
]