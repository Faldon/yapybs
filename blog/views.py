from django.shortcuts import render
from .models import BlogPost
import datetime


def index(request, page=1):
    """ Index View
    :param request: HTTP Request
    :param page: Page number to view
    :return: HTTP Response
    """
    selected_posts = BlogPost.objects.order_by('published')[5*(int(page)-1):5*int(page)]
    post_count = BlogPost.objects.count()

    return render(request, 'blog/index.html', dict(
        selected_posts=selected_posts,
        current_date=datetime.date.today(),
        current_page=int(page),
        page_count=range(0, int(round(post_count/5)+1)))
    )


def year_archive(request, year, page=1):
    """ Year archive view
    :param request: HTTP Request
    :param year: Year to view
    :param page: Page number to view
    :return: HTTP Response
    """
    selected_posts = BlogPost.objects.filter(
        published__gte=datetime.date(int(year), 1, 1)).exclude(
            published__gte=datetime.date(int(year)+1, 1, 1)
        ).order_by('published')[5*(int(page)-1):5*int(page)]
    post_count = BlogPost.objects.filter(
        published__gte=datetime.date(int(year), 1, 1)).exclude(
            published__gte=datetime.date(int(year)+1, 1, 1)
        ).count()

    return render(request, 'blog/year_archive.html', dict(
        selected_posts=selected_posts,
        current_date=datetime.date.today(),
        current_page=int(page),
        selected=datetime.date(int(year), 1, 1),
        page_count=range(0, int(round(post_count/5)+1)))
    )


def month_archive(request, year, month, page=1):
    """ Month archive view
    :param request: HTTP Request
    :param year: Year to view
    :param month: Month to view
    :param page: Page number to view
    :return: HTTP Response
    """
    selected_posts = BlogPost.objects.filter(
        published__gte=datetime.date(int(year), int(month), 1)).exclude(
            published__gte=datetime.date(int(year), int(month)+1, 1)
        ).order_by('published')[5*(int(page)-1):5*int(page)]
    post_count = BlogPost.objects.filter(
        published__gte=datetime.date(int(year), int(month), 1)).exclude(
            published__gte=datetime.date(int(year), int(month)+1, 1)
        ).count()

    return render(request, 'blog/month_archive.html', dict(
        selected_posts=selected_posts,
        current_date=datetime.date.today(),
        current_page=int(page),
        selected=datetime.date(int(year), int(month), 1),
        page_count=range(0, int(round(post_count/5)+1)))
    )


def day_archive(request, year, month, day):
    """  Day archive view
    :param request: HTTP Request
    :param year: Year to view
    :param month: Month to view
    :param day: Day to view
    :return: HTTP Response
    """
    selected_posts = BlogPost.objects.filter(published=datetime.date(int(year), int(month), int(day)))

    return render(request, 'blog/day_archive.html', dict(selected_posts=selected_posts, current_date=datetime.date.today()))


def detail(request, post_id):
    """ Post details view
    :param request: HTTP Request
    :param post_id: ID of blog post
    :return: HTTP Response
    """
    post = BlogPost.objects.get(pk=post_id)

    return render(request, 'blog/post.html', dict(post=post, current_date=datetime.date.today()))