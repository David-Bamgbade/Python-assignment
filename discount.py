price  = (input('Enter Price'))
float(price)

discount_percentage = (input('Enter Discount'))
float(discount_percentage)

discount = float(discount_percentage) / 100 * float(price)
float(discount)

price_after_discount = float(price) - float(discount)
float(price_after_discount)

print('The price after discount', 'is', price_after_discount)