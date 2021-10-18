from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.blog_detail, name='blog-detail'),
    path('<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]

