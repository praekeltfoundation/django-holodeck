django-holodeck
===============

Pushes stats to holodeck

required settings
*****************

Please add the following to you `settings` file::

    from datetime import datetime
    HOLODECK_API = {
        'holodeck_server': 'http://holodeck.praekelt.com',
        'ga_profile_id': 'xxx',
        'cumulative_start_date': datetime(year=2013, month=1, day=1), #project start date
        'users_types': 'xxx',
        'users_cumulative': 'xxx',
        'pageviews_weekly': 'xxx',
        'pageviews_cumulative': 'xxx',
    }
