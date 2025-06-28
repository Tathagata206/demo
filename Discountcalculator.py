price=float(input("Enter the price of your product: "))
discount=float(input("Enter the discount percentage of your product: "))
discount_amount=(discount/100)*price
final_price= price - discount_amount
print(final_price)