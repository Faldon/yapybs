from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost
import datetime


def index(request, page=1):
    selected_posts = BlogPost.objects.order_by('published')[5*(page-1):5*page]
    post_count = BlogPost.objects.count()

    return render(request, 'blog/index.html', dict(
        selected_posts=selected_posts,
        current_date=datetime.date.today(),
        current_page=page,
        page_count=range(0, int(round(post_count/5)+1)))
    )


def month_archive(request, year, month):
    latest_posts = BlogPost.objects.filter(
        published__gte=datetime.date(year, month, 1)).exclude(
            published__gte=datetime.date(year, month+1, 1)
        )

    return render(request, 'blog/index.html', dict(latest_posts=latest_posts, current_date=datetime.date.today()))


def day_archive(request, year, month, day):
    latest_posts = BlogPost.objects.filter(published=datetime.date(year, month, day))

    return render(request, 'blog/index.html', dict(latest_posts=latest_posts, current_date=datetime.date.today()))


def year_archive(request, year):
    latest_posts = BlogPost.objects.filter(published__year=year)

    return render(request, 'blog/index.html', dict(latest_posts=latest_posts, current_date=datetime.date.today()))


def detail(request, post_id):
    post = BlogPost.objects.get(pk=post_id)

    return render(request, 'blog/post.html', dict(post=post, current_date=datetime.date.today()))
    return None