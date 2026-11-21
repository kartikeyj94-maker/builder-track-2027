
import json


def calculate_progress(completed, total):
    if total == 0:
        return 0

    return (completed / total) * 100


def customer_health(progress):
    if progress == 100:
        return "Fully onboarded"
    elif progress >= 75:
        return "On track"
    elif progress >= 50:
        return "Needs attention"
    else:
        return "At risk"


with open("customers.json", "r") as file:
    customers = json.load(file)


print("CUSTOMER ONBOARDING PORTFOLIO")

for customer in customers:

    print("\nCompany:", customer["company"])
    print("Owner:", customer["owner"])

    completed_count = 0

    for number, requirement in enumerate(
        customer["requirements"], start=1
    ):
        task = requirement["task"]
        status = requirement["status"]

        print(f"{number}. [{status}] {task}")

        if status == "Completed":
            completed_count += 1

    total_tasks = len(customer["requirements"])

    progress = calculate_progress(completed_count, total_tasks)
    health = customer_health(progress)

    print(f"Onboarding progress: {progress:.0f}%")
    print(f"Customer health: {health}")
    print("-" * 40)
