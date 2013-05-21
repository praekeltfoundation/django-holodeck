from django.conf import settings
from datetime import datetime, timedelta
from google_credentials import utils
from photon import Client
from celery import task
from holodeck import actions


@task(ignore_result=True)
def push():
    if not hasattr(settings, 'HOLODECK_API'):
        raise Exception("Imporperly configured. Please specify `HOLODECK_API` dict as per the documention")

    range_end = datetime.now()
    range_start = range_end - timedelta(days=7)

    client = Client(server=settings.HOLODECK_API.get('holodeck_server'))
    ga_service = utils.get_service()

    actions.push_users_types(ga_service, client, range_start, range_end)
    actions.push_users_cummulative(ga_service, client, range_start, range_end)
    actions.push_pageviews_weekly(ga_service, client, range_start, range_end)
    actions.push_pageviews_cumulative(ga_service, client, range_start, range_end)
