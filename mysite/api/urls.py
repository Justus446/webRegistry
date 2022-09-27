#api/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'patients', views.patient_view)
router.register(r'persons', views.person_view)
router.register(r'items', views.item_view)
router.register(r'roles', views.role_view)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('patients/', include('rest_framework.urls', namespace='rest_framework')),
    path('patients/', views.patient_view, name='patients'),
    path('items/', views.item_view, name='items'),
    path('persons/', views.person_view, name='persons'),
    path('persons/', include('rest_framework.urls', namespace='rest_framework')),
    path('roles/', include('rest_framework.urls', namespace='rest_framework')),
    path('items/', include('rest_framework.urls', namespace='rest_framework'))
]
