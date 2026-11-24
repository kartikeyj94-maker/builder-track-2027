try:
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    if price <=0:
        print("Price must be greater than zero.")

    elif quantity <= 0:
        print("Quantity must be greater than zero.")

    else:
        total = price * quantity
        print(f"Total price: {total:.2f}")

except ValueError:
    print("Error: Please enter valid numbers.")
 