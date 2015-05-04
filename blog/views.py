import datetime

from django.shortcuts import render, redirect
from django.db.models import Q

from .models import BlogPost
from .forms import DatepickerForm


def index(request, page='1'):
    """ Index View

    Selects the nth 5 posts where n is the given page number and renders the index page.

    :type request: django.http.HttpRequest
    :type page: string
    :param request: The http request sent from the client
    :param page: Page number to view
    :return: An html http response
    :rtype: django.http.HttpResponse
    """
    selected_posts = BlogPost.objects.order_by('-published')[(int(page) - 1) * 5:5 * int(page)]

    # Count total number of posts
    post_count = BlogPost.objects.count()

    return render(request, 'blog/index.html', dict(
        selected_posts=selected_posts,
        current_page=int(page),
        page_count=range(0, (post_count/5)+(post_count % 5)*1)
        )
    )


def year_archive(request, year, page='1'):
    """ Year archive view

    Selects the nth 5 posts published in given year where n is the given page number and renders the year archive page.

    :type request: django.http.HttpRequest
    :type year: string
    :type page: string
    :param request: The http request sent from the client
    :param year: Year to view
    :param page: Page number to view
    :return: An html http response
    :rtype: django.http.HttpResponse
    """
    # Get posts published in the given year
    selected_posts = BlogPost.objects.filter(
        published__gte=datetime.date(int(year), 1, 1)).exclude(
        published__gte=datetime.date(int(year) + 1, 1, 1)
    ).order_by('-published')[5 * (int(page) - 1):5 * int(page)]

    # Count number of posts in the given year
    post_count = BlogPost.objects.filter(
        published__gte=datetime.date(int(year), 1, 1)).exclude(
        published__gte=datetime.date(int(year) + 1, 1, 1)
    ).count()

    return render(request, 'blog/year_archive.html', dict(
        selected_posts=selected_posts,
        current_page=int(page),
        selected=datetime.date(int(year), 1, 1),
        page_count=range(0, (post_count/5)+(post_count % 5)*1)
        )
    )


def month_archive(request, year, month, page='1'):
    """ Month archive view

    Selects the nth 5 posts published in given month and given year where n is the given page number
    and renders the month archive page.

    :type request: django.http.HttpRequest
    :type year: string
    :type month: string
    :type page: string
    :param request: The http request sent from the client
    :param year: Year to view
    :param month: Month to view
    :param page: Page number to view
    :return: An html http response
    :rtype: django.http.HttpResponse

    """
    # Get first of current month
    current_month = datetime.date(int(year), int(month), 1)

    # Get first of previous month
    previous_month = current_month - datetime.timedelta(days=1)
    previous_month.replace(day=1)

    # Get first of next month
    next_month = current_month + datetime.timedelta(days=31)
    next_month.replace(day=1)

    # Get posts published in the current month
    selected_posts = BlogPost.objects.filter(
        published__gte=current_month
    ).exclude(
        published__gte=next_month
    ).order_by('-published')[5 * (int(page) - 1):5 * int(page)]

    # Count number of posts in the current month
    post_count = BlogPost.objects.filter(
        published__gte=current_month
    ).exclude(
        published__gte=next_month
    ).count()

    return render(request, 'blog/month_archive.html', dict(
        selected_posts=selected_posts,
        current_page=int(page),
        selected=current_month,
        previous_month=previous_month,
        next_month=next_month,
        page_count=range(0, (post_count/5)+(post_count % 5)*1)
        )
    )


def day_archive(request, year, month, day):
    """  Day archive view

    Selects all posts published at date build by given year,month and day and renders the day archive page or
    processes the form data on POST and redirects to itself.

    :type request: django.http.HttpRequest
    :type year: string
    :type month: string
    :type day: string
    :param request: The http request sent from the client
    :param year: Year to view
    :param month: Month to view
    :param day: Day to view
    :return: A http redirect or an html http response
    :rtype: django.http.HttpResponseRedirect or django.http.HttpResponse
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
            published__gte=datetime.date(int(year), int(month), int(day) + 1)
        ).order_by('-published')

        return render(request, 'blog/day_archive.html', dict(
            selected_posts=selected_posts,
            selected=datetime.date(int(year), int(month), int(day)),
            form=form)
        )


def detail(request, post_id):
    """ Post details view

    Selects the post with the given id and renders the post page.

    :type request: django.http.HttpRequest
    :type post_id: string
    :param request: The http request sent from the client
    :param post_id: ID of blog post
    :return: An html http response
    :rtype: django.http.HttpResponse
    """
    post = BlogPost.objects.get(pk=post_id)

    return render(request, 'blog/post.html', dict(post=post))


def rss(request):
    """ RSS feed view

    Returns an rss feed of the latest fifteen posts.

    :type request: django.http.HttpRequest
    :param request: The http request sent from the client
    :return: An xml http response
    :rtype: django.http.HttpRequest
    """
    posts = BlogPost.objects.order_by('-published')[:15]

    return render(request, 'blog/rss.xml', dict(posts=posts), content_type='text/xml')


def search(request):
    """ Search view

    Finds all blog posts which have a tag assigned equal to the keyword(s) submitted or which topics contains parts
    of the keyword(s) submitted

    :type request: django.http.HttpRequest
    :param request: The http request sent from the client
    :return: An html http response
    :rtype: django.http.HttpRequest
    """
    selected_posts = BlogPost.objects.filter(
        Q(tags__name__iexact=request.POST['search']) | Q(topic__icontains=request.POST['search'])
    )

    return render(request, 'blog/search.html', dict(
        selected_posts=selected_posts,
        keywords=request.POST['search'])
    )