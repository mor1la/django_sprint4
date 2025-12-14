from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post

POSTS_PER_PAGE = 5


def index(request):
    post_list = (
        Post.objects.select_related('author', 'category', 'location')
        .filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True,
        )
        .order_by('-pub_date')[:POSTS_PER_PAGE]
    )
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.select_related('author', 'category', 'location'),
        pk=id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = (
        Post.objects.select_related('author', 'category', 'location')
        .filter(
            category=category,
            is_published=True,
            pub_date__lte=timezone.now(),
        )
        .order_by('-pub_date')
    )
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
