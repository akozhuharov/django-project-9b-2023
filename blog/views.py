from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import PostForm
from .models import Post


class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, "post_create.html", {"form": form})
    
    def post(self, request):
        data = request.POST
        form = PostForm(data)
        if not form.is_valid():
            return HttpResponse("Not proper form", status=400)
        form.save()
        return redirect("/")




def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})