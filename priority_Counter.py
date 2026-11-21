scores = [95, 45, 82, 60, 91, 35]

priority_count = 0

for score in scores:
    if score >= 80:
        priority_count += 1

print("Total priority leads:", priority_count)