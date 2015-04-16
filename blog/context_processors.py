import datetime
from django.conf import settings


def current_date(request):
    return {
        'current_date': datetime.date.today()
    }


def brand_text(request):
    return {
        'brand_text': getattr(settings, "BRAND_TEXT", "")
    }


def site_title(request):
    return {
        'site_title': getattr(settings, "SITE_TITLE", "")
    }