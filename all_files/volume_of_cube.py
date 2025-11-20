
def cube(sides):                            # Defines the function
    volume = sides **3                      # Defines the volume
    surface_area = 6 * (sides **2)          # Defines the surface_area

    return volume, surface_area             # Define what to be returned in a tuple

returned_values = cube(8)

print(f"The volume and surface_area are {returned_values} respectively")

print(type(returned_values))