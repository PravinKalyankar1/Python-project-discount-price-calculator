# Discount price calculator
Item= input("Enter the name of item:")
Price_of_item= float(input("Enter the price of item:"))
Discount_of_item= float(input("Discount percentage:"))

Discount_amount=Price_of_item* Discount_of_item/100
Final_price=Price_of_item-Discount_amount
print("Final price of item:", Final_price)