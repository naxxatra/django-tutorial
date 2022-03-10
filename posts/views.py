from django.views import generic
from posts.models import Posts


class PostListView(generic.ListView):
    """
    View to see all the posts in a list
    """

    model = Posts
    queryset = Posts.objects.all().order_by("-created_at")
    template_name = "posts/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All Posts"
        return context


class PostDetailView(generic.DetailView):
    """
    View to see a single post in detail
    """

    model = Posts
    template_name = "posts/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.title
        return context
