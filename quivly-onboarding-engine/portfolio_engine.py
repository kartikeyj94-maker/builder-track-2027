
import json


# Calculate onboarding progress
def calculate_progress(completed, total):
    if total == 0:
        return 0
    return (completed / total) * 100


# Classify customer health
def customer_health(progress):
    if progress == 100:
        return "Fully onboarded"
    elif progress >= 75:
        return "On track"
    elif progress >= 50:
        return "Needs attention"
    else:
        return "At risk"


# Run the customer onboarding report
def main():

    # Load customer data safely
    try:
        with open("customers.json", "r") as file:
            customers = json.load(file)

    except FileNotFoundError:
        print("Error: Customer data file not found.")
        raise SystemExit(1)

    except json.JSONDecodeError:
        print("Error: Customer data contains invalid JSON.")
        raise SystemExit(1)

    print("CUSTOMER ONBOARDING PORTFOLIO")

    onboarding_report = []

    # Process each customer
    for customer in customers:

        print("\nCompany:", customer["company"])
        print("Owner:", customer["owner"])

        completed_count = 0

        # Process onboarding requirements
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

        # Store the results
        result = {
            "company": customer["company"],
            "owner": customer["owner"],
            "progress": progress,
            "health": health,
            "remaining_tasks": remaining_tasks
        }

        onboarding_report.append(result)

        # Display results
        print(f"Onboarding progress: {progress:.0f}%")
        print(f"Customer health: {health}")
        print(f"Remaining tasks: {remaining_tasks}")
        print("-" * 40)

    # Export report to JSON
    with open("onboarding_report.json", "w") as file:
        json.dump(onboarding_report, file, indent=4)

    print("\nOnboarding report saved successfully.")


# Run main only when executed directly
if __name__ == "__main__":
    main()
