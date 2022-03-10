from django.contrib import admin
from posts.models import Posts


class PostsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)
    ordering = ("-id",)


admin.site.register(Posts, PostsAdmin)
