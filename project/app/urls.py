from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('blog_post/<str:pk>', views.blog_post, name="blog_post"),
    path('projects/', views.projects, name="projects"),
    path('project/<str:pk>', views.project, name="project"),
    path('tags/', views.tags, name="tags"),
    path('tags/<str:pk>', views.tag, name="tag"),
    path('kontaktai/', views.kontaktai, name="kontaktai"),
    path('about/', views.about, name="about"),
]
