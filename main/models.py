from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Author(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    info = models.TextField(max_length=200, help_text='write sth about yourself!')

    class Meta:
        ordering = ['user_name']

    def get_absolute_url(self):
        return reverse('blogs-by-author', args=[str(self.id)])

    def __str__(self):
        return self.user_name.username


class Post(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=2000, help_text='Write the story here!')
    image = models.URLField(null=True)

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Comment(models.Model):
    # post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=1000, help_text='Enter your comment here.')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    sentiment = models.IntegerField(default=0)

    def approve(self):
        self.approved = True

    def __str__(self):
        return self.content

