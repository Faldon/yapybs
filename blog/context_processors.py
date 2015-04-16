import datetime
from django.conf import settings


def current_date(request):
    return {
        'current_date' : datetime.date.today()
    }


def brand_text(self):
    return {
        'brand_text' : getattr(settings, "BRAND_TEXT", "")
    }