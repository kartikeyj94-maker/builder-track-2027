companies = ["HubSpot", "Salesforce", "Clay", "Apollo"]

priority_companies = ["HubSpot", "Salesforce", "Apollo"]

for company in companies:
    if company in priority_companies:
        print(company, "is a priority lead")
    else:
        print(company, "is a regular lead")