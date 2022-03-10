from posts.views import PostListView, PostDetailView
from django.urls import path

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
]
