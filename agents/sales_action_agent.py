def recommend_sales_action(company, persona, intent_stage):

    actions = []

    if intent_stage == "Evaluation":
        actions.append("Prioritize account for immediate outbound outreach")
        actions.append("Research VP Sales or Revenue Operations leaders")
        actions.append("Send personalized case studies relevant to the industry")

    elif intent_stage == "Consideration":
        actions.append("Add company to targeted outbound campaign")
        actions.append("Share product comparison or solution guides")
        actions.append("Monitor further visitor activity")

    else:
        actions.append("Add account to nurture marketing campaign")
        actions.append("Share educational blog content")
        actions.append("Track future engagement signals")

    return actions