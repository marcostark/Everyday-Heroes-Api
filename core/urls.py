from django.urls import path
from . import views

urlpatterns = [
    path('collect-point/', views.CollectPointListView.as_view())
]