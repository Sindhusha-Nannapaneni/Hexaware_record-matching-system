from dateutil import parser
import re

def normalize_text(text):
    if not text:
        return ""
    return re.sub(r"\s+", " ", text.lower().strip())

def parse_datetime(date, time=None):
    try:
        if not date:
            return None

        if time:
            dt = parser.parse(f"{date} {time}")
        else:
            dt = parser.parse(date)

        return dt.replace(tzinfo=None)
    except:
        return None

def normalize_location(location):
    if not location:
        return "unknown"

    location = location.lower()

    if any(x in location for x in ["zoom", "teams", "virtual"]):
        return "virtual"

    return location.strip()