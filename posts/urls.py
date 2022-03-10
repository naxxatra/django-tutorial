from django.urls import path
from posts.views import PostDetailView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("<int:pk>/", PostDetailView.as_view(), name="detail"),
]
