import random

companies = [
    {
        "name": "BrightPath Lending",
        "domain": "brightpathlending.com",
        "industry": "Mortgage Lending",
        "size": "200 employees",
        "hq": "Chicago, USA",
        "founding_year": 2012,
        "description": "BrightPath Lending provides digital mortgage lending solutions that streamline the home financing process for buyers across the United States."
    },
    {
        "name": "Summit Realty Group",
        "domain": "summitrealty.com",
        "industry": "Real Estate",
        "size": "350 employees",
        "hq": "Denver, USA",
        "founding_year": 2008,
        "description": "Summit Realty Group offers residential and commercial real estate brokerage services while leveraging modern digital property search tools."
    },
    {
        "name": "Rocket Mortgage",
        "domain": "rocketmortgage.com",
        "industry": "Mortgage Finance",
        "size": "5000 employees",
        "hq": "Detroit, USA",
        "founding_year": 1985,
        "description": "Rocket Mortgage is one of the largest digital mortgage lenders in the United States, providing fully online home loan experiences."
    },
    {
        "name": "Redfin",
        "domain": "redfin.com",
        "industry": "Real Estate Technology",
        "size": "4000 employees",
        "hq": "Seattle, USA",
        "founding_year": 2004,
        "description": "Redfin is a technology-powered real estate brokerage that combines online home search tools with real estate agent services."
    },
    {
        "name": "Compass Real Estate",
        "domain": "compass.com",
        "industry": "Real Estate Brokerage",
        "size": "3000 employees",
        "hq": "New York, USA",
        "founding_year": 2012,
        "description": "Compass is a modern real estate platform that provides technology tools for real estate agents, buyers, and sellers."
    }
]

def identify_company(visitor):
    company = random.choice(companies)
    return company