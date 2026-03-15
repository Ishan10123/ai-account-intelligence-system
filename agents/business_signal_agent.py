import random

signals = [
    "Company recently hiring sales roles",
    "Expansion into new regional markets",
    "Recent funding announcement",
    "Growth in product offerings",
    "Partnership announcements"
]

def detect_business_signals(company):
    return random.sample(signals, 2)