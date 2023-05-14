from django.urls import path
from . import views

# add app name if you use in template "{% url 'app_name:name_part of urls.py file' %}" like this this format

app_name = "blog"

urlpatterns = [
    path(route="", view=views.post_list, name="postpage"),
    path(route="single_post/<int:pk>/", view=views.post_detail, name='post_detail'),
]
