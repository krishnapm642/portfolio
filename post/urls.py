from django.urls import path
from .views import contactview, IndexView

urlpatterns = [
    path('contact/', contactview, name = 'contact'),

    path('', IndexView.as_view(), name = 'indexclass'),
]
