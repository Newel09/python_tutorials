
def x(y: int, z: int) -> int:
    return ((y/z) / 10 * z) # Defines formula with the variables

modulos = x(10,3) # Gives values to the variables in the function

temp = x(20, 2)
print(modulos)
print(temp)