

import json
from pathlib import Path

config_path = Path(__file__).with_name("icp_config.json")

with open(config_path, "r") as file:
    CONFIG = json.load(file)# WEEK 3 - DAY 3
# Python ICP Lead Scoring Engine

# 1. Score company size (maximum 30 points)

def score_company_size(employees):
    rules = CONFIG["company_size"]

    if rules["min_employees"] <= employees <= rules["max_employees"]:
        return rules["points"]
    return 0


def score_industry(industry):
    rules = CONFIG["industry"]

    if industry == rules["target"]:
        return rules["points"]
    return 0


def score_geography(country):
    rules = CONFIG["geography"]

    if country == rules["target"]:
        return rules["points"]
    return 0


def score_buying_signal(hiring_support):
    rules = CONFIG["buying_signal"]

    if hiring_support == rules["hiring_support"]:
        return rules["points"]
    return 0

# 5. Calculate total ICP score
def calculate_icp_score(employees, industry, country, hiring_support):
    size_score = score_company_size(employees)
    industry_score = score_industry(industry)
    geography_score = score_geography(country)
    signal_score = score_buying_signal(hiring_support)

    total_score = size_score + industry_score + geography_score + signal_score

    return total_score


# 6. Classify lead priority
def classify_lead(score):
    if score >= 80:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"


# 7. Run the program
if __name__ == "__main__":

    print("COMPANY SIZE TESTS")
    print(score_company_size(120))
    print(score_company_size(1000))

    print("\nINDUSTRY TESTS")
    print(score_industry("B2B SaaS"))
    print(score_industry("Manufacturing"))

    print("\nGEOGRAPHY TESTS")
    print(score_geography("United States"))
    print(score_geography("India"))

    print("\nBUYING SIGNAL TESTS")
    print(score_buying_signal(True))
    print(score_buying_signal(False))

    print("\nTOTAL ICP SCORE TESTS")
    print(calculate_icp_score(120, "B2B SaaS", "United States", True))
    print(calculate_icp_score(1000, "Manufacturing", "India", False))

    print("\nLEAD PRIORITY TESTS")
    print(classify_lead(100))
    print(classify_lead(60))
    print(classify_lead(30))
    print(classify_lead(80))

    print("\nFULL COMPANY SCORING EXAMPLE")

    score = calculate_icp_score(
        120,
        "B2B SaaS",
        "United States",
        True
    )

    priority = classify_lead(score)

    print(f"ICP Score: {score}/100")
    print(f"Lead Priority: {priority}")
