from dateutil import parser

def normalize_text(text):
    if not text:
        return ""
    return text.lower().strip()

def parse_datetime(date, time=None):

    try:

        if time:
            dt = parser.parse(f"{date} {time}")
        else:
            dt = parser.parse(date)

        # Remove timezone info
        return dt.replace(tzinfo=None)

    except:
        return None


def normalize_location(location):

    if not location:
        return "unknown"

    location = location.lower()

    if "zoom" in location:
        return "virtual"

    if "teams" in location:
        return "virtual"

    if "virtual" in location:
        return "virtual"

    return location.strip()