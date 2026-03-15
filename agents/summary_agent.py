def generate_summary(visitor, persona, intent_score, intent_stage):

    city = visitor["location"]["city"]
    country = visitor["location"]["country"]

    pages = ", ".join(visitor["pages_visited"])

    summary = f"""
Visitor activity detected from {city}, {country}.

Browsing behavior includes the following pages:
{pages}

The visitor is likely a {persona}. Behavioral signals indicate an intent score of {intent_score}, placing them in the {intent_stage} stage of the buying journey.

This account may represent a potential opportunity for outreach.
"""

    return summary.strip()