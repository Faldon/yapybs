import datetime
from django.conf import settings


def current_date(request):
    """
    Returns the current date for using in templates
    :param request: HTTP Request
    :return:
    """
    return {
        'current_date': datetime.date.today()
    }


def brand_text(request):
    """
    Returns the brand_text from settings for using in templates
    :param request:
    :return:
    """
    return {
        'brand_text': getattr(settings, "BRAND_TEXT", "")
    }


def site_title(request):
    """
    Returns the site_title from settings for using in templates
    :param request:
    :return:
    """
    return {
        'site_title': getattr(settings, "SITE_TITLE", "")
    }