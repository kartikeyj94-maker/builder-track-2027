
# Step 1: Our companies and their scores
companies = ["HubSpot", "Clay", "Apollo", "Notion", "Stripe"]
scores = [95, 82, 45, 90, 70]

# Step 2: Start with three empty buckets
hot_count = 0
warm_count = 0
cold_count = 0

# Step 3: Check each company one by one
for i in range(len(companies)):

    if scores[i] >= 80:
        print(companies[i], "is a Hot lead")
        hot_count = hot_count + 1

    elif scores[i] >= 50:
        print(companies[i], "is a Warm lead")
        warm_count = warm_count + 1

    else:
        print(companies[i], "is a Cold lead")
        cold_count = cold_count + 1

# Step 4: Show how many leads are in each bucket
print("Hot leads:", hot_count)
print("Warm leads:", warm_count)
print("Cold leads:", cold_count)