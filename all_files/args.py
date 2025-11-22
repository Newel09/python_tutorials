
def my_var_sum(*args):      # Function with a variable argument

    sum = 0
    for arg in args:        # Define argument
        sum += arg          # Argument function
    return sum

sum = my_var_sum(220,340,450, 400,10000)

print(sum)