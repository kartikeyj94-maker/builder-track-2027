companies = ["HubSpot", "Clay", "Apollo", "Notion"]
scores = [95, 45, 82, 60]

threshold = 80
priority_count = 0

for i in range(len(companies)):
    if scores[i] >= threshold:
        print(companies[i], "is a priority lead")
        priority_count += 1
    else:
        print(companies[i], "is a regular lead")
print("Total priority leads:", priority_count)
print("Total leads checked:", len(scores))

qualification_rate = (priority_count / len(scores)) * 100
print(f"Qualification rate: {qualification_rate}%")
