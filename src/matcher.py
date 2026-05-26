from difflib import SequenceMatcher
from src.features import normalize_text, parse_datetime


class RecordMatcher:

    # ---------------- SCORE ONE PAIR ----------------
    def calculate_match(self, crm, cal):

        crm_text = normalize_text(crm.get("subject"))
        cal_text = normalize_text(cal.get("title"))

        crm_company = normalize_text(crm.get("client_company"))
        cal_title = normalize_text(cal.get("title"))

        crm_owner = normalize_text(crm.get("relationship_owner"))
        cal_attendees = " ".join(cal.get("attendees", [])).lower()

        crm_dt = parse_datetime(crm.get("meeting_date"), crm.get("meeting_time"))
        cal_dt = parse_datetime(cal.get("start_time"))

        # ---------------- FEATURES ----------------
        text_score = SequenceMatcher(None, crm_text, cal_text).ratio()
        company_score = SequenceMatcher(None, crm_company, cal_title).ratio()

        time_score = 0
        if crm_dt and cal_dt:
            diff_hours = abs((crm_dt - cal_dt).total_seconds()) / 3600
            time_score = max(0, 1 - diff_hours / 6)

        attendee_score = 1 if crm_owner.replace(" ", "") in cal_attendees.replace(" ", "") else 0

        # ---------------- FINAL SCORE ----------------
        final_score = (
            0.45 * time_score +
            0.30 * text_score +
            0.20 * company_score +
            0.05 * attendee_score
        )

        return {
            "match": final_score >= 0.68,
            "confidence": round(final_score, 3)
        }

    # ---------------- FILTER PAIRS (IMPORTANT STABILITY FIX) ----------------
    def is_candidate(self, crm, cal):

        crm_text = normalize_text(crm.get("subject"))
        cal_text = normalize_text(cal.get("title"))

        crm_company = normalize_text(crm.get("client_company"))
        cal_title = normalize_text(cal.get("title"))

        crm_dt = parse_datetime(crm.get("meeting_date"), crm.get("meeting_time"))
        cal_dt = parse_datetime(cal.get("start_time"))

        text_sim = SequenceMatcher(None, crm_text, cal_text).ratio()
        company_sim = SequenceMatcher(None, crm_company, cal_title).ratio()

        time_sim = 0
        if crm_dt and cal_dt:
            diff_hours = abs((crm_dt - cal_dt).total_seconds()) / 3600
            time_sim = max(0, 1 - diff_hours / 6)

        # REQUIRE 2 STRONG SIGNALS
        strong_count = 0

        if text_sim >= 0.65:
            strong_count += 1
        if company_sim >= 0.65:
            strong_count += 1
        if time_sim >= 0.65:
            strong_count += 1

        return strong_count >= 2

    # ---------------- MAIN PIPELINE ----------------
    def find_matches(self, crm_records, cal_records):

        predictions = []

        for crm in crm_records:

            for cal in cal_records:

                # STEP 1: FILTER
                if not self.is_candidate(crm, cal):
                    continue

                # STEP 2: SCORE
                result = self.calculate_match(crm, cal)

                predictions.append({
                    "crm_id": crm.get("crm_id"),
                    "calendar_id": cal.get("event_id"),
                    "match": result["match"],
                    "score": result["confidence"]
                })

        return predictions