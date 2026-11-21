# Builder Track 2027

## Week 1 — Python Foundations

My first four programs:

- **hello.py** — Collects a name and city.
- **tip_calculator.py** — Calculates a restaurant tip.
- **unit_converter.py** — Converts Celsius to Fahrenheit.
- **string_cleaner.py** — Cleans company names.

## Week 2 — Python CSV & RevOps Automation

Built my first working CSV lead-cleaning pipeline using Python.

**What it does:**
- Reads lead records from a CSV file.
- Identifies missing company names and invalid lead scores.
- Removes duplicate companies, including differences in capitalisation.
- Classifies leads as priority or regular based on their scores.
- Calculates lead qualification rates.
- Exports cleaned records into a new CSV file.
- Uses a basic assertion to verify the validated lead count.

**Test results (synthetic data):**
- 7 input records
- 4 unique, valid leads
- 3 priority leads
- 75% clean-lead qualification rate

**Files:**
- [csv_lead_reader.py](csv_lead_reader.py) — Python validation and cleaning script.
- [leads.csv](leads.csv) — Sample input data.
- [clean_leads.csv](clean_leads.csv) — Cleaned output data.

**What I learned:** Python loops, conditionals, dictionaries, lists, sets, exception handling, CSV reading/writing, basic assertions and debugging.

Also completed two introductory Exercism Python exercises: *Hello World* and *Guido's Gorgeous Lasagna*.

**Next:** Reusable functions, automated testing, SQL and CRM automation.


## Week 2 — Customer Onboarding & Health Classification

### Quivly Customer Onboarding Engine

Built a Python-based customer onboarding automation
tool that processes multiple SaaS customer accounts
and identifies accounts requiring attention.

**Features:**

- Structured customer data processing using JSON.
- Automated onboarding progress calculation.
- Multi-customer processing using nested loops.
- Reusable Python functions and business logic.
- Rule-based customer health classification.
- Defensive programming and edge-case testing.

**Test results (synthetic customer data):**

| Customer | Progress | Health Status |
|---|---:|---|
| Acme Technologies | 75% | On track |
| Nova Health | 50% | Needs attention |
| Orbit AI | 100% | Fully onboarded |

All four progress calculation scenarios passed,
including zero-task customers.

**Technical skills:** Python, JSON, functions,
nested loops, conditional logic, debugging,
Git, GitHub and project documentation.

[View project and documentation](./quivly-onboarding-engine)

## Additional Technical Learning

- Postman API Beginner Learning Path — Completed.
- HubSpot CRM data hygiene and lifecycle governance
  — Four practical labs completed.
- CRM data validation using synthetic customer records.
- Git version control and remote synchronisation.

## Next

- Automated testing with pytest.
- Configurable ICP and lead scoring.
- Portfolio-level customer reporting.
- HubSpot API integration.
- Clay enrichment and GTM automation.
- AI-powered workflows and cloud deployment.
