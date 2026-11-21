scores = [95, 45, 82, 60, 91, 35]

threshold = int(input("Enter minimum lead score: "))

priority_count = 0

for score in scores:
    if score >= threshold:
        priority_count += 1

print("Total priority leads:", priority_count)
print("Total leads checked:", len(scores))

qualification_rate = (priority_count / len(scores)) * 100
print(f"Qualification rate: {qualification_rate:.1f}%")