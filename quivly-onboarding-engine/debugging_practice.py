
import json


# Calculate onboarding completion percentage
def calculate_progress(completed, total):
    if total == 0:
        return 0

    return (completed / total) * 100


# Classify customer health based on onboarding progress
def customer_health(progress):
    if progress == 100:
        return "Fully onboarded"
    elif progress >= 75:
        return "On track"
    elif progress >= 50:
        return "Needs attention"
    else:
        return "At risk"


# Load customer data from JSON
with open("customers.json", "r") as file:
    customers = json.load(file)


print("CUSTOMER ONBOARDING PORTFOLIO")

# Create an empty list to store customer results
onboarding_report = []


# Process each customer
for customer in customers:

    print("\nCompany:", customer["company"])
    print("Owner:", customer["owner"])

    completed_count = 0

    # Process each customer's onboarding tasks
    for number, requirement in enumerate(
        customer["requirements"], start=1
    ):
        task = requirement["task"]
        status = requirement["status"]

        print(f"{number}. [{status}] {task}")

        if status == "Completed":
            completed_count += 1

    # Calculate onboarding metrics
    total_tasks = len(customer["requirements"])
    remaining_tasks = total_tasks - completed_count

    progress = calculate_progress(completed_count, total_tasks)
    health = customer_health(progress)

    # Store results in a dictionary
    result = {
        "company": customer["company"],
        "owner": customer["owner"],
        "progress": progress,
        "health": health,
        "remaining_tasks": remaining_tasks
    }

    # Add customer results to the report
    onboarding_report.append(result)

    # Display customer results
    print(f"Onboarding progress: {progress:.0f}%")
    print(f"Customer health: {health}")
    print(f"Remaining tasks: {remaining_tasks}")
    print("-" * 40)


# Export all customer results to JSON
with open("onboarding_report.json", "w") as file:
    json.dump(onboarding_report, file, indent=4)

print("\nOnboarding report saved successfully.")
