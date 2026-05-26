from fuzzywuzzy import fuzz


def text_similarity(a, b):

    if not a or not b:
        return 0

    return fuzz.token_set_ratio(a, b) / 100


def time_similarity(t1, t2):

    if not t1 or not t2:
        return 0.5

    try:
        # Remove timezone info if present
        t1 = t1.replace(tzinfo=None)
        t2 = t2.replace(tzinfo=None)

        diff_hours = abs((t1 - t2).total_seconds()) / 3600

        return max(0, 1 - (diff_hours / 24))

    except:
        return 0


def attendee_similarity(client_name, attendees):

    if not client_name or not attendees:
        return 0

    client_name = client_name.lower()

    for attendee in attendees:

        attendee = attendee.lower()

        if client_name.replace(" ", ".") in attendee:
            return 1

    return 0


def location_similarity(l1, l2):

    if not l1 or not l2:
        return 0

    l1 = l1.lower()
    l2 = l2.lower()

    if l1 == l2:
        return 1

    if "virtual" in l1 and "virtual" in l2:
        return 1

    if "zoom" in l1 and "zoom" in l2:
        return 1

    if "teams" in l1 and "teams" in l2:
        return 1

    return 0