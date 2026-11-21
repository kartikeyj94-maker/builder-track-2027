import json

with open("customer.json", "r") as file:
    customer = json.load(file)

print("ONBOARDING PLAN")
print("Company:", customer["company"])
print("Owner:", customer["owner"])
print()

status = "In Progress"

for number, requirement in enumerate(customer["requirements"], start=1):
    print(f"{number}. [{status}] {requirement}")