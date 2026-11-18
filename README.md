# Builder Track 2027

## Week 1 — Python Foundations

My first four programs:

- **hello.py** — Collects a name and city.
- **tip_calculator.py** — Calculates a restaurant tip.
- **unit_converter.py** — Converts Celsius to Fahrenheit.
- **string_cleaner.py** — Cleans company names.

- ## Week 2 — Python CSV & RevOps Automation

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
