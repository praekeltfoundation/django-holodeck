from django.conf import settings
from datetime import datetime


def push_users_types(ga_service, client, range_start, range_end, ref_date):
    print "Pushing Mobi Users Types"

    query = ga_service.data().ga().get(
        ids='ga:%d' % settings.HOLODECK_API.get('ga_profile_id'),
        start_date=str(range_start.date()),
        end_date=str(range_end.date()),
        metrics='ga:visitors',
        dimensions='ga:visitorType',
    )

    results = query.execute()
    if 'rows' in results:
        client.send(
            samples=[(row[0], int(row[1])) for row in results['rows']],
            api_key=settings.HOLODECK_API.get('users_types'),
            timestamp=ref_date,
        )


def push_users_cummulative(ga_service, client, range_start, range_end, ref_date):
    print "Pushing Mobi Users Cumulative"

    range_start_cumulative = datetime(year=2013, month=1, day=1,
                                      hour=0, minute=0, second=0)
    query = ga_service.data().ga().get(
        ids='ga:%d' % settings.HOLODECK_API.get('ga_profile_id'),
        start_date=str(range_start_cumulative.date()),
        end_date=str(range_end.date()),
        metrics='ga:visitors',
    )

    results = query.execute()
    client.send(
        samples=(
            ("Users", results['totalsForAllResults']['ga:visitors']),
        ),
        api_key=settings.HOLODECK_API.get('users_cumulative'),
        timestamp=ref_date,
    )


def push_pageviews_weekly(ga_service, client, range_start, range_end, ref_date):
    print "Pushing Mobi Weekly Pageviews"

    query = ga_service.data().ga().get(
        ids='ga:%d' % settings.HOLODECK_API.get('ga_profile_id'),
        start_date=str(range_start.date()),
        end_date=str(range_end.date()),
        metrics='ga:pageviews'
    )

    results = query.execute()
    client.send(
        samples=(
            ("Pageviews", results['totalsForAllResults']['ga:pageviews']),
        ),
        api_key=settings.HOLODECK_API.get('pageviews_weekly'),
        timestamp=ref_date,
    )


def push_pageviews_cumulative(ga_service, client, range_start, range_end, ref_date):
    print "Pushing Mobi Pageviews Cumulative"

    range_start_cumulative = settings.HOLODECK_API.get('cumulative_start_date')

    query = ga_service.data().ga().get(
        ids='ga:%d' % settings.HOLODECK_API.get('ga_profile_id'),
        start_date=str(range_start_cumulative.date()),
        end_date=str(range_end.date()),
        metrics='ga:pageviews',
    )

    results = query.execute()
    client.send(
        samples=(
            ("Pageviews", results['totalsForAllResults']['ga:pageviews']),
        ),
        api_key=settings.HOLODECK_API.get('pageviews_cumulative'),
        timestamp=ref_date,
    )
