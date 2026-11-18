
import csv

with open("leads.csv", "r") as file:
    reader = csv.DictReader(file)

    # Initialize counters
    priority_count = 0
    total_leads = 0
    invalid_count = 0
    duplicate_count = 0
    missing_company_count = 0
    unique_valid_count = 0

    seen_companies = set()
    clean_leads = []

    for row in reader:
        total_leads += 1
        company = row["company"].strip()
        company_key = company.casefold()

        # Check for missing company names
        if company == "":
            missing_company_count += 1
            print("Missing company name")
            continue

        # Check for duplicate companies
        if company in seen_companies:
            duplicate_count += 1
            print(company, "is a duplicate")
            continue

        # Validate the lead score
        try:
            score = int(row["score"])
        except (ValueError, TypeError):
            invalid_count += 1
            print(company, "has an invalid or missing score")
            continue

        # Remember only companies with valid scores
        seen_companies.add(company)
        unique_valid_count += 1
        clean_leads.append({"company": company, "score": score})

        # Classify the lead
        if score >= 80:
            priority_count += 1
            print(company, "is a priority lead")
        else:
            print(company, "is a regular lead")


# Report lead counts
print("Total priority leads:", priority_count)
print("Total leads checked:", total_leads)
print("Invalid scores:", invalid_count)
print("Missing company names:", missing_company_count)
print("Duplicate records:", duplicate_count)
print("Validated unique leads:", unique_valid_count)


# Calculate qualification rate across all records
if total_leads > 0:
    qualification_rate = (priority_count / total_leads) * 100
else:
    qualification_rate = 0

print(f"Overall qualification rate: {qualification_rate:.1f}%")


# Calculate qualification rate among unique valid leads
if unique_valid_count > 0:
    clean_qualification_rate = (priority_count / unique_valid_count) * 100
else:
    clean_qualification_rate = 0

print(f"Clean-lead qualification rate: {clean_qualification_rate:.1f}%")
print("Clean leads:", clean_leads)
with open("clean_leads.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["company", "score"])
    writer.writeheader()
    writer.writerows(clean_leads)

print("Clean leads exported to clean_leads.csv")
assert len(clean_leads) == unique_valid_count
print("Test passed: exported lead count matches validated lead count")