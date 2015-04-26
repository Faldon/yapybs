from django.shortcuts import render, redirect
from django.db.models import Q
from .models import BlogPost
from .forms import DatepickerForm
import datetime


def index(request, page=1):
    """ Index View
    :param request: HTTP Request
    :param page: Page number to view
    :return: HTTP Response
    """
    selected_posts = BlogPost.objects.order_by('-published')[5*(int(page)-1):5*int(page)]
    post_count = BlogPost.objects.count()

    return render(request, 'blog/index.html', dict(
        selected_posts=selected_posts,
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
        ).order_by('-published')[5*(int(page)-1):5*int(page)]
    post_count = BlogPost.objects.filter(
        published__gte=datetime.date(int(year), 1, 1)).exclude(
            published__gte=datetime.date(int(year)+1, 1, 1)
        ).count()

    return render(request, 'blog/year_archive.html', dict(
        selected_posts=selected_posts,
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
        ).order_by('-published')[5*(int(page)-1):5*int(page)]
    post_count = BlogPost.objects.filter(
        published__gte=datetime.date(int(year), int(month), 1)).exclude(
            published__gte=datetime.date(int(year), int(month)+1, 1)
        ).count()

    return render(request, 'blog/month_archive.html', dict(
        selected_posts=selected_posts,
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
    if request.method == 'POST':
        form = DatepickerForm(request.POST)
        if form.is_valid():
            date_selected = form.cleaned_data['dateselector']
            return redirect('day_archive', year=date_selected.year, month=date_selected.month, day=date_selected.day)
    else:
        form = DatepickerForm()
        selected_posts = BlogPost.objects.filter(
            published__gte=datetime.date(int(year), int(month), int(day))).exclude(
                published__gte=datetime.date(int(year), int(month), int(day)+1)
            ).order_by('-published')

        return render(request, 'blog/day_archive.html', dict(
            selected_posts=selected_posts,
            selected=datetime.date(int(year), int(month), int(day)),
            form=form)
        )


def detail(request, post_id):
    """ Post details view
    :param request: HTTP Request
    :param post_id: ID of blog post
    :return: HTTP Response
    """
    post = BlogPost.objects.get(pk=post_id)

    return render(request, 'blog/post.html', dict(post=post))


def rss(request):
    """ RSS feed view
    :param request: HTTP Request
    :return: HTTP Response
    """
    posts = BlogPost.objects.order_by('-published')[:15]

    return render(request, 'blog/rss.xml', dict(posts=posts), content_type='text/xml')


def search(request):
    selected_posts = BlogPost.objects.filter(
        Q(tags__name__iexact=request.POST['search']) | Q(topic__icontains=request.POST['search'])
    )

    return render(request, 'blog/search.html', dict(
        selected_posts=selected_posts,
        keywords=request.POST['search'])
    )