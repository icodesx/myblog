from django.urls import path
from . import views
from .views import IndexView, PostView, AddPostView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('article/<int:pk>', PostView.as_view(), name='post'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
]
