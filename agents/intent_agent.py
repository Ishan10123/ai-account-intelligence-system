def calculate_intent(visitor):

    score = 0
    pages = visitor["pages_visited"]

    if "/pricing" in pages:
        score += 3

    if "/demo-request" in pages:
        score += 3

    if "/ai-sales-agent" in pages:
        score += 2

    if "/case-studies" in pages:
        score += 1

    if visitor["visits_this_week"] >= 3:
        score += 1

    if score >= 7:
        stage = "Evaluation"
    elif score >= 4:
        stage = "Consideration"
    else:
        stage = "Research"

    return score, stage