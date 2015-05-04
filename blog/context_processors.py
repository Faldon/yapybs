import datetime
from django.conf import settings


def current_date(request):
    """ Returns the current date for using in templates

    :type request: django.http.HttpRequest
    :param request: The http request sent from the client
    :return: The current date as value to key current_date
    :rtype: dict
    """
    return dict(current_date=datetime.date.today())


def brand_text(request):
    """ Returns the brand text provided in settings for using in templates

    :type request: django.http.HttpRequest
    :param request: The http request sent from the client
    :return: The BRAND_TEXT from settings as value to key brand_text
    :rtype: dict
    """
    return dict(brand_text=getattr(settings, "BRAND_TEXT", ""))


def site_title(request):
    """ Returns the site title provided in settings for using in templates

    :type request: django.http.HttpRequest
    :param request: The http request sent from the client
    :return: The SITE_TITLE from settings as value to key sute_title
    :rtype: dict
    """
    return dict(site_title=getattr(settings, "SITE_TITLE", ""))