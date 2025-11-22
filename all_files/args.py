
def my_var_sum(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

sum = my_var_sum(220,340,450, 400,10000)

print(sum)