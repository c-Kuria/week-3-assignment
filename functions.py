def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discountedPrice = price * (discount_percent/100)
        print(f"Discount: Ksh {discountedPrice}")
        print(f"Total Amount: Ksh {price - discountedPrice}")
    else:
        print(f"Total Amount: Ksh {price}")

price = int(input("Enter Original Amount: Ksh "))
discount_percent = int(input("Enter Discount Percentage: "))

if discount_percent > 100:
    print("The discount percentage should be less or equal to 100%")
else:
    calculate_discount(price,discount_percent)
