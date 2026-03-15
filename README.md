# AI Account Intelligence & Enrichment System

## Overview

Sales and marketing teams frequently face two major problems:

1. Anonymous website visitors provide little actionable insight.
2. Incomplete company data makes it difficult to prioritize accounts.

This project builds an **AI-powered account intelligence system** that converts raw visitor signals into **structured company intelligence and recommended sales actions**.

The system processes visitor behavior signals and automatically generates:

- Company identification
- Persona inference
- Intent scoring
- Company enrichment
- Technology stack detection
- Leadership discovery
- Business signals
- AI-generated account summary
- Recommended sales actions

The final results are visualized through an **interactive Streamlit dashboard**.

---

## Example Input

Visitor activity data:

```
Visitor ID: 001
IP: 34.201.xxx.xxx

Pages visited:
- /pricing
- /ai-sales-agent
- /case-studies

Time on site: 3m 42s
Visits this week: 3
Device: desktop
Location: Austin, USA
```

---

## Example Output

```
Company: BrightPath Lending
Domain: brightpathlending.com
Industry: Mortgage Lending
Company Size: 200 employees
Headquarters: Chicago, USA

Persona: Sales Leader
Intent Score: 7
Intent Stage: Evaluation

Technology Stack:
CRM: Salesforce
Marketing: HubSpot
Website: WordPress
Analytics: Google Analytics

Leadership:
CEO: Michael Carter
VP Sales: Amanda Cole
Head of Marketing: David Lee
RevOps: Sarah Mitchell

Business Signals:
- Hiring sales roles
- Market expansion

Recommended Sales Actions:
- Prioritize account for outreach
- Research VP Sales or RevOps
- Send industry case studies
```

---

# System Architecture

```
Visitor Traffic Simulation
        ↓
Company Identification Agent
        ↓
Persona Inference Agent
        ↓
Intent Scoring Engine
        ↓
Company Enrichment
        ↓
Technology Stack Detection
        ↓
Leadership Discovery
        ↓
Business Signals Detection
        ↓
Sales Action Recommendation
        ↓
Account Intelligence Dashboard
```

---

# Features

### Company Identification
Maps visitor signals to likely companies using enrichment agents.

### Persona Inference
Infers visitor role based on browsing behavior.

Example:
- Pricing page → Buyer
- Docs page → Technical persona
- Blog → Researcher

### Intent Scoring
Scores likelihood that a visitor is in an active buying journey.

### Company Enrichment
Generates company profile data including:
- Domain
- Industry
- Company size
- Headquarters
- Founding year
- Business description

### Technology Stack Detection
Detects company technologies such as:
- CRM
- Marketing automation
- Website platform
- Analytics tools

### Leadership Discovery
Identifies potential decision makers:
- CEO
- VP Sales
- Head of Marketing
- RevOps leader

### Business Signals
Detects signals indicating growth or opportunity:
- Hiring activity
- Partnerships
- Market expansion

### AI Account Summary
Generates structured intelligence describing visitor behavior and company fit.

### Recommended Sales Actions
Provides clear next steps for sales teams.

### Real-Time Visitor Monitoring
The dashboard simulates live visitor activity to highlight high-intent accounts.

---

# Dashboard

The Streamlit dashboard provides:

- Account intelligence leaderboard
- Intent score analytics
- Account intelligence cards
- Leadership and technology insights
- Sales action recommendations
- Real-time visitor simulation

---

# Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/ai-account-intelligence-system.git
cd ai-account-intelligence-system
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Run the System

Generate visitor dataset:

```
python dataset_generator.py
```

Run the intelligence pipeline:

```
python -m pipeline.intelligence_pipeline
```

Launch the dashboard:

```
streamlit run dashboard.py
```

---

# Future Improvements

This prototype uses simulated enrichment data. In a production system, the enrichment agents could integrate with:

- Reverse IP lookup services
- Public enrichment APIs (Clearbit, Apollo, ZoomInfo)
- Web scraping pipelines
- LLM research agents

---

# Technologies Used

- Python
- Streamlit
- Pandas

---

# Demo

A short Loom demo explains the system architecture and shows the dashboard in action.

```