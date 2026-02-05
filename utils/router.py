def route_claim(fields: dict, missing_fields: list, raw_text: str):
    text = raw_text.lower()

    # Priority 1: Missing fields
    if missing_fields:
        return (
            "Manual Review",
            "Mandatory fields missing: " + ", ".join(missing_fields)
        )

    # Priority 2: Fraud keywords
    if any(word in text for word in ["fraud", "staged", "inconsistent"]):
        return (
            "Investigation Flag",
            "Suspicious keywords detected in incident description"
        )

    # Priority 3: Injury claims
    if fields.get("claim_type") == "injury":
        return (
            "Specialist Queue",
            "Claim involves injury and requires specialist handling"
        )

    # Priority 4: Low damage
    if fields.get("estimated_damage") and fields["estimated_damage"] < 25000:
        return (
            "Fast-track",
            "Estimated damage below threshold for fast-track processing"
        )

    return (
        "Manual Review",
        "Default routing applied"
    )
