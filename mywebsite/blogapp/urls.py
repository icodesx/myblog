from django.urls import path
from . import views
from .views import IndexView, PostView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('article/<int:pk>', PostView.as_view(), name='post'),
]
