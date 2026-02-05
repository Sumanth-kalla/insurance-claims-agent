import re

MANDATORY_FIELDS = [
    "policy_number",
    "claim_type",
    "estimated_damage",
    "description"
]

def extract_fields(text: str) -> dict:
    data = {}

    # Policy information
    data["policy_number"] = _regex(text, r"Policy Number[:\- ]*(\w+)")
    data["policyholder_name"] = _regex(text, r"Name of Insured[:\- ]*(.+)")
    data["effective_dates"] = _regex(text, r"Effective Dates[:\- ]*(.+)")

    # Incident information
    data["date_of_loss"] = _regex(text, r"Date of Loss[:\- ]*(\d{2}/\d{2}/\d{4})")
    data["time_of_loss"] = _regex(text, r"Time[:\- ]*(\d{2}:\d{2})")
    data["location"] = _regex(text, r"Location of Loss[:\- ]*(.+)")
    data["description"] = _regex(text, r"Description[:\- ]*(.+)")

    # Asset details
    data["asset_type"] = "vehicle" if "vehicle" in text.lower() else "property"
    data["asset_id"] = _regex(text, r"VIN[:\- ]*(\w+)")
    data["estimated_damage"] = _extract_amount(text)

    # Claim type
    data["claim_type"] = "injury" if "injur" in text.lower() else "vehicle"

    # Attachments (simple assumption)
    data["attachments"] = "yes" if "attachment" in text.lower() else "no"
    data["initial_estimate"] = data["estimated_damage"]

    return data


def find_missing_fields(fields: dict) -> list:
    missing = []
    for field in MANDATORY_FIELDS:
        if not fields.get(field):
            missing.append(field)
    return missing


def _regex(text: str, pattern: str):
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else None


def _extract_amount(text: str):
    match = re.search(r"Estimate Amount[:\- ]*\$?([\d,]+)", text, re.IGNORECASE)
    if match:
        return int(match.group(1).replace(",", ""))
    return None
