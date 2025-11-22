# import from bill_function.py

from library_system.bill_function import total_calc

bill_amount = float(input("Enter bill amount: "))
total = total_calc(bill_amount)
    
print(f"Please pay ${total}")

