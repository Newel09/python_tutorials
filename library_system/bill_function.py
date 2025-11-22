def total_calc(bill_amount, tip_perc = 10):
    return round(bill_amount * (1 + (0.01 * tip_perc)),2)