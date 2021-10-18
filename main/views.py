from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from .forms import CommentForm
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions
from .text2speech import *

# Create your views here.


def index(request):

    num_post = Post.objects.all().count()
    posts = Post.objects.all()

    context = {
        'num_post': num_post,
        'posts': posts
    }

    return render(request, 'index.html', context=context)


def blog_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(Post=pk)
    text2speech(post.content, 'post'+str(pk)+'.wav')
    post_path = 'post'+str(pk)+'.wav'
    i = 0
    approved = []
    for c in comments:
        if c.is_approved:
            path = 'comment'+str(pk)+'-'+str(i)+'.wav'
            print(path)
            text2speech(c.content, path)
            dic = {'author': c.author, 'content': c.content, 'path': path}
            approved.append(dic)
            i += 1
    print(approved)
    return render(request, 'post_detail.html', context={'post': post, 'comments': approved, 'post_path': post_path})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Post = post
            print(comment.content)
            response = text_analysis(comment.content)
            json_text = json.dumps(response, indent=2)
            print(json_text)
            anger = response['keywords'][0]['emotion']
            sentiment = response['keywords'][0]['sentiment']['label']
            print(anger)
            print(sentiment)
            if sentiment == 'positive':
                comment.is_approved = True
            comment.save()
            return redirect(index)

    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})

