
def greet(name: str = None):    # Greet a person by name, defaulting to "world".
    if name is None:
        name = "world"
    print(f"Hello, {name}!")
greet("Newel")

