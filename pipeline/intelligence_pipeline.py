import json
import random

from agents.intent_agent import calculate_intent
from agents.persona_agent import infer_persona
from agents.summary_agent import generate_summary

from agents.company_identifier import identify_company

from agents.tech_stack_agent import detect_tech_stack
from agents.sales_action_agent import recommend_sales_action

from agents.business_signal_agent import detect_business_signals
from agents.leadership_agent import discover_leadership


def analyze_visitor(visitor):

    company = identify_company(visitor)

    intent_score, intent_stage = calculate_intent(visitor)

    persona = infer_persona(visitor)
    
    behavior_signals = visitor["pages_visited"]

    tech_stack = detect_tech_stack(company)

    summary = generate_summary(visitor, persona, intent_score, intent_stage)

    sales_actions = recommend_sales_action(company, persona, intent_stage)

    business_signals = detect_business_signals(company)

    leadership = discover_leadership(company)

    persona_confidence = random.randint(65, 92)
    company_match_confidence = random.randint(70, 95)

    result = {
        "visitor_id": visitor["visitor_id"],
        "company": company["name"],
        "domain": company["domain"],
        "industry": company["industry"],
        "company_size": company["size"],
        "headquarters": company["hq"],
        "founding_year": company["founding_year"],
        "business_description": company["description"],

        "technology_stack": tech_stack,
        "leadership": leadership,

        "business_signals": business_signals,
        "behavior_signals": behavior_signals,

        "location": visitor["location"],
        "persona": persona,
        "intent_score": intent_score,
        "intent_stage": intent_stage,

        "ai_summary": summary,
        "recommended_sales_actions": sales_actions
    }

    return result


def run_pipeline():

    with open("visitor_dataset.json") as f:
        visitors = json.load(f)

    results = []

    for visitor in visitors[:20]:
        result = analyze_visitor(visitor)
        results.append(result)

    with open("account_intelligence_output.json", "w") as f:
        json.dump(results, f, indent=2)

    print("AI Account Intelligence report generated.")


if __name__ == "__main__":
    run_pipeline()