from django.urls import path
from . import views
from django.views.generic.base import TemplateView, RedirectView

urlpatterns = [
    path('ex1/', TemplateView.as_view(template_name='ex1.html', extra_context={'title': 'Custom title'})),
    path('ex2/', views.Ex2View.as_view(), name='ex2'),
    path('rdt/', RedirectView.as_view(url='https://google.com'), name='go-to-google'),   # 1 - way
    path('', RedirectView.as_view(pattern_name='ex2')),   # 2 - way
    path('add-view/<int:pk>/', views.PostPreLoaderView.as_view(), name='add-view'),
    path('single/<int:pk>/', views.SinglePageView.as_view(), name='single'),

]
