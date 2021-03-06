from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import HashTag, Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        # content, image, hashtag 모두 포함되어야한다.
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # save를 잠시 멈춰둔다.
            post.user = request.user
            # post object (None)
            post.save()
            # post object (1) # id를 부여
            for word in post.content.split():
                if word.startswith('#'):
                    # hashtag 추가
                    # hashtag, created = Hashtag.objects.get_or_create(content=word) # (obj, True or False)
                    hashtag = HashTag.objects.get_or_create(content=word)[0]
                    post.hashtags.add(hashtag)
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)

@login_required
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        return redirect('posts:index')

def update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.hashtags.clear() # HashTag를 다시 연결해준다.
            for word in post.content.split():
                if word.startswith('#'):
                    # hashtag 추가
                    # hashtag, created = Hashtag.objects.get_or_create(content=word) # (obj, True or False)
                    hashtag = HashTag.objects.get_or_create(content=word)[0]
                    post.hashtags.add(hashtag)
            return redirect('posts:index')
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)

def hashtags(request, id):
    hashtag = get_object_or_404(HashTag, id=id)

    posts = hashtag.taged_post.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/all.html', context)

@login_required
def like(request, id):
    post = get_object_or_404(Post, id=id)
    user = request.user
    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return redirect('posts:feed')

def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'posts/feed.html', context)

@login_required
def detail_like(request, id):
    post = get_object_or_404(Post, id=id)
    user = request.user
    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return redirect('posts:detail', id)

def all(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/all.html', context)

# def all(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 5)
#     page = request.GET.get('page')
#     posts = paginator.get_page(page)
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'posts/pagination.html', context)