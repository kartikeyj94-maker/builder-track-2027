companies = ["HubSpot", "Clay", "Apollo", "Notion", "Stripe"]
scores = [95, 82, 60, 90, 40]

for i in range(len(companies)):
    if scores[i] >= 80:
        print(companies[i], "is a Hot lead")
    elif scores[i] >= 50:
        print(companies[i], "is a Warm lead")
    else:
        print(companies[i], "is a Cold lead")