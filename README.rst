django-holodeck
---------------

Pushes stats to holodeck

required settings
`````````````````

Please add the following to you `settings` file::

    from datetime import datetime
    HOLODECK_API = {
        'holodeck_server': 'http://holodeck.praekelt.com',
        'ga_profile_id': 'xxx',
        'cumulative_start_date': datetime(year=2013, month=1, day=1), #project start date
        
        #holodeck metric API keys
        'users_types': 'xxx',           # Pie Chart
        'users_cumulative': 'xxx',      # Line Chart (could also be a guage)
        'pageviews_weekly': 'xxx',      # Line Chart
        'pageviews_cumulative': 'xxx',  # Line Chart
    }
