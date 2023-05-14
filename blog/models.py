from django.db import models
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        # reverse(app_name:name_part of the urls.py file)
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    