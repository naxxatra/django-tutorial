from django.views import generic
from posts.models import Posts

class PostListView(generic.ListView):
    """
    View to see all the posts in a list
    """
    model = Posts
    queryset = Posts.objects.all().order_by('-created_at')
    template_name = 'posts/index.html'

class PostDetailView(generic.DetailView):
    """
    View to see a single post in detail
    """
    model = Posts
    template_name = 'posts/detail.html'