from datetime import datetime, timedelta

def parse_date_range(query: str):
    """Parse simple relative dates like 'yesterday', 'last week', 'today'."""
    now = datetime.now()

    if "yesterday" in query.lower():
        start = now - timedelta(days=1)
        end = now - timedelta(days=1)
    elif "last week" in query.lower():
        start = now - timedelta(days=7)
        end = now
    elif "today" in query.lower():
        start = now
        end = now
    else:
        # default: last 3 days
        start = now - timedelta(days=3)
        end = now

    return start.date(), end.date()
