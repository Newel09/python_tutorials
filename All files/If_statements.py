"""
fruit_price = 40,50,55,60,70,90,120,150,170,200

IF fruit_price < 40:
    print("cheap")
ELSE IF fruit_price < 70:
    print("price is good")
ELSE IF fruit_price <= 90:
    print("expensive)
ELSE:
    print("very expensive")
"""

allowed_prices = {40, 50, 55, 60, 70, 90, 120, 150, 170, 200}

fruit_price = int(input("Enter the price fruit price: "))

if all(fruit_price < 40 for n in allowed_prices): # print "Cheap" is fruit_price is less than 40
    print("Cheap"),
elif all(fruit_price < 70 for n in allowed_prices): # print "Price is good" if price is less than 70
    print("Price is good"),
elif all(fruit_price <= 90 for n in allowed_prices): # prints "Expensive" if price is less or equal to 90
    print("Expensive"),
else:
    print("Very expensive")