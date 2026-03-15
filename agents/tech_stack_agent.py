import random

tech_stacks = [
    {
        "CRM": "Salesforce",
        "Marketing": "HubSpot",
        "Website": "WordPress",
        "Analytics": "Google Analytics"
    },
    {
        "CRM": "HubSpot CRM",
        "Marketing": "Marketo",
        "Website": "Webflow",
        "Analytics": "Google Analytics"
    },
    {
        "CRM": "Zoho CRM",
        "Marketing": "Mailchimp",
        "Website": "WordPress",
        "Analytics": "Mixpanel"
    },
    {
        "CRM": "Salesforce",
        "Marketing": "Pardot",
        "Website": "Drupal",
        "Analytics": "Google Analytics"
    }
]

def detect_tech_stack(company):

    return random.choice(tech_stacks)