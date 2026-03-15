import random

ceos = [
    "Michael Carter",
    "Jonathan Reed",
    "Robert Williams",
    "Sophia Martinez",
    "Daniel Thompson"
]

vp_sales = [
    "Amanda Cole",
    "Emily Parker",
    "Laura Bennett",
    "Kevin Walker",
    "Brian Mitchell"
]

marketing_heads = [
    "David Lee",
    "Daniel Chen",
    "Kevin Zhang",
    "Rachel Adams",
    "Olivia Turner"
]

revops_heads = [
    "Sarah Mitchell",
    "Chris Thompson",
    "Nathan Scott",
    "Ryan Hall",
    "Jessica Moore"
]


def discover_leadership(company):

    leadership = {
        "CEO": random.choice(ceos),
        "VP Sales": random.choice(vp_sales),
        "Head of Marketing": random.choice(marketing_heads),
        "RevOps": random.choice(revops_heads)
    }

    return leadership