from django.shortcuts import render
from .models import Blog_post, Projects, Tag

# Create your views here.


def home(request):
    return render(request, 'app/home.html')


def kontaktai(request):
    return render(request, 'app/kontaktai.html')


def about(request):
    return render(request, 'app/about.html')


def blog(request):

    # posts = Blog_post.objects.all()
    posts = Blog_post.objects.filter(active=True)

    context = {'posts': posts}
    return render(request, 'app/blog.html', context)


def blog_post(request, pk):
    post = Blog_post.objects.get(id=pk)

    context = {'post': post}
    return render(request, 'app/blog_post.html', context)


def projects(request):

    projects = Projects.objects.filter(active=True)

    context = {'projects': projects}
    return render(request, 'app/projects.html', context)


def project(request, pk):
    project = Projects.objects.get(id=pk)

    context = {'project': project}
    return render(request, 'app/project.html', context)


def tags(request):
    tags = Tag.objects.all()

    context = {'tags': tags}
    return render(request, 'app/tags.html', context)


def tag(request, pk):
    tag = Tag.objects.get(id=pk)
    postauskai = tag.blog_post_set.all()

    # postauskai = Blog_post.objects.filter(tags__name='emacs')
    context = {'tag': tag, 'postauskai': postauskai}
    return render(request, 'app/tag.html', context)
