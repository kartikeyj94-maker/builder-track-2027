
import csv

with open("leads.csv", "r") as file:
    reader = csv.DictReader(file)

    priority_count = 0
    total_leads = 0
    invalid_count = 0
    seen_companies = set()

    for row in reader:
        total_leads += 1
        company = row["company"]

        if company in seen_companies:
            print(company, "is a duplicate")
        else:
            seen_companies.add(company)

        try:
            score = int(row["score"])

        except ValueError:
            invalid_count += 1
            print(row["company"], "has an invalid or missing score")
            continue

        if score >= 80:
            priority_count += 1
            print(row["company"], "is a priority lead")
        else:
            print(row["company"], "is a regular lead")

print("Total priority leads:", priority_count)
print("Total leads checked:", total_leads)
print("Invalid leads:", invalid_count)

if total_leads > 0:
    qualification_rate = (priority_count / total_leads) * 100
else:
    qualification_rate = 0

print(f"Qualification rate: {qualification_rate:.1f}%")
valid_leads = total_leads - invalid_count

if valid_leads > 0:
    valid_qualification_rate = (priority_count / valid_leads) * 100
else:
    valid_qualification_rate = 0

print("Valid leads:", valid_leads)
print(f"Valid-lead qualification rate: {valid_qualification_rate:.1f}%")