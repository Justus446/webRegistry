# api/urls.py
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('facilities/', views.facility_list),
    path('facilities/<int:pk>/', views.facility_detail),
    path('clients/', views.client_list),
    path('clients/<int:pk>/', views.client_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)
