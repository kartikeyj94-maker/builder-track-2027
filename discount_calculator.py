def calculate_final_price(price, discount):
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    return final_price
price = float(input("Enter product price: "))
print(price)
discount = float(input("Enter discount percentage: "))
print(discount)
discount_amount = price * discount / 100
print(discount_amount)
final_price = price - discount_amount
print(f"Final price: {final_price:.2f}")
