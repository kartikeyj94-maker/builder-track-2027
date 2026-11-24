
import csv

from icp_scorer import calculate_icp_score, classify_lead

# Fictional companies for safe testing
companies = [
    {
        "name": "Alpha AI Demo",
        "domain": "alpha.example.com",
        "employees": 120,
        "industry": "B2B SaaS",
        "country": "United States",
        "hiring_support": True
    },
    {
        "name": "Beta Cloud Demo",
        "domain": "beta.example.com",
        "employees": 350,
        "industry": "B2B SaaS",
        "country": "India",
        "hiring_support": False
    },
    {
        "name": "Gamma Tech Demo",
        "domain": "gamma.example.com",
        "employees": 1000,
        "industry": "Manufacturing",
        "country": "India",
        "hiring_support": False
    }
]

with open("icp_scores.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Company name",
        "Company domain name",
        "ICP Score",
        "Lead Priority",
        "ICP Review Status"
    ])

    for company in companies:
        score = calculate_icp_score(
            company["employees"],
            company["industry"],
            company["country"],
            company["hiring_support"]
        )

        priority = classify_lead(score)

        writer.writerow([
            company["name"],
            company["domain"],
            score,
            priority,
            "Pending Review"
            
        ])

        print(company["name"], score, priority)

print("CSV export complete.")
