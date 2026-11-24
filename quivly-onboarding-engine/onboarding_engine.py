import json

def calculate_progress(completed, total):
    if total == 0:
        return 0
        completed_count
        total_tasks

    return (completed / total) * 100

with open("customer.json", "r") as file:
    customer = json.load(file)

print("ONBOARDING PLAN")
print("Company:", customer["company"])
print("Owner:", customer["owner"])
print()

completed_count = 0

for number, requirement in enumerate(customer["requirements"], start=1):
    task = requirement["task"]
    status = requirement["status"]
    print(f"{number}. [{status}] {task}")
    if status == "Completed":
        completed_count += 1

total_tasks = len(customer["requirements"])

progress = calculate_progress(completed_count, total_tasks)

print(f"\nOnboarding progress: {progress:.0f}%")

