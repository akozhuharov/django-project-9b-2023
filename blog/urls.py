from django.urls import path
from blog.views import index, PostCreateView

urlpatterns = [
    path('', view=index, name="index"),
    path("create/", view=PostCreateView.as_view(), name="post-create")
]
