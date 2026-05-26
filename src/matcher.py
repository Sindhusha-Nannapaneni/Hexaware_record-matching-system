from src.preprocess import *
from src.features import *

class RecordMatcher:

    def __init__(self):
        self.threshold = 0.65

    def calculate_match(self, crm, cal):

        crm_subject = normalize_text(crm.get("subject"))
        cal_title = normalize_text(cal.get("title"))

        crm_company = normalize_text(crm.get("client_company"))
        crm_notes = normalize_text(crm.get("notes"))

        cal_description = normalize_text(cal.get("description"))

        crm_location = normalize_location(crm.get("location"))
        cal_location = normalize_location(cal.get("location"))

        crm_datetime = parse_datetime(
            crm.get("meeting_date"),
            crm.get("meeting_time")
        )

        cal_datetime = parse_datetime(
            cal.get("start_time")
        )

        # Feature Scores
        time_score = time_similarity(crm_datetime, cal_datetime)

        text_score = text_similarity(
            crm_subject + " " + crm_notes,
            cal_title + " " + cal_description
        )

        company_score = text_similarity(
            crm_company,
            cal_title
        )

        attendee_score = attendee_similarity(
            crm.get("client_name"),
            cal.get("attendees")
        )

        location_score = location_similarity(
            crm_location,
            cal_location
        )

        # Weighted Final Score
        final_score = (
            0.30 * time_score +
            0.25 * attendee_score +
            0.20 * company_score +
            0.15 * text_score +
            0.10 * location_score
        )

        return {
            "match": final_score >= self.threshold,
            "confidence": round(final_score, 3)
        }

    def find_matches(self, crm_records, cal_records):

        matches = []

        for crm in crm_records:
            for cal in cal_records:

                result = self.calculate_match(crm, cal)

                if result["match"]:

                    matches.append({
                        "crm_id": crm["crm_id"],
                        "calendar_id": cal["event_id"],
                        "score": result["score"]
                    })

        return matches