import json
import random
import uuid
from datetime import datetime, timedelta

pages_pool = [
    "/",
    "/pricing",
    "/ai-sales-agent",
    "/product",
    "/case-studies",
    "/blog",
    "/docs",
    "/contact",
    "/demo-request",
    "/integration"
]

referral_sources = [
    "google",
    "linkedin",
    "direct",
    "twitter",
    "newsletter",
    "bing"
]

devices = [
    "desktop",
    "mobile",
    "tablet"
]

cities = [
    "New York",
    "San Francisco",
    "Chicago",
    "Austin",
    "Boston",
    "Seattle"
]

countries = [
    "USA",
    "Canada",
    "UK"
]

def random_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

def random_time():
    minutes = random.randint(1, 6)
    seconds = random.randint(0, 59)
    return f"{minutes}m {seconds}s"

def generate_pages():
    num_pages = random.randint(1, 5)
    return random.sample(pages_pool, num_pages)

def generate_timestamp():
    now = datetime.now()
    delta = timedelta(minutes=random.randint(1, 1440))
    return (now - delta).isoformat()

def generate_visitor():
    return {
        "visitor_id": str(uuid.uuid4())[:8],
        "ip": random_ip(),
        "pages_visited": generate_pages(),
        "time_on_site": random_time(),
        "visits_this_week": random.randint(1, 5),
        "referral_source": random.choice(referral_sources),
        "device": random.choice(devices),
        "location": {
            "city": random.choice(cities),
            "country": random.choice(countries)
        },
        "timestamp": generate_timestamp()
    }

def generate_dataset(num_visitors=50):
    visitors = [generate_visitor() for _ in range(num_visitors)]
    return visitors

if __name__ == "__main__":
    dataset = generate_dataset(100)

    with open("visitor_dataset.json", "w") as f:
        json.dump(dataset, f, indent=2)

    print("Visitor dataset generated successfully.")