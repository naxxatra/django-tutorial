from django.db import models
from django.utils.translation import gettext_lazy as _


class Posts(models.Model):
    """
    Model for the posts
    """

    title = models.CharField("Title of the post", max_length=200)
    content = models.TextField("Content of the post")
    created_at = models.DateTimeField("Created at", auto_now=True, editable=True)
    cover = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = _("Posts")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
