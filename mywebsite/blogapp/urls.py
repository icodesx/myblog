from django.urls import path
from . import views
from .views import IndexView, PostView, AddPostView, EditPostView, DeletePostView, AddCategoryView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('article/<int:pk>', PostView.as_view(), name='post'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('article/<int:pk>/edit', EditPostView.as_view(), name='edit-post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    path('add-category/', AddCategoryView.as_view(), name='add-category')
]
