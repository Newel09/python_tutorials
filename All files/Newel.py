"""Loop examples collected in one file.

This keeps the original simple loop behavior and adds several
additional loop examples (range, enumerate, while, nested loops,
for-else, generators, and list comprehensions) so the file demonstrates
many common loop patterns.
"""

fruits = ["apple", "banana", "cherry", "date"]


def basic_for():
    """Original behaviour: iterate and use continue/break."""
    print("basic_for:")
    for f in fruits:
        if f == "banana":
            continue   # skip printing banana
        if f == "date":
            break      # stop the loop when we reach date
        print(f)
    print()


def for_with_range():
    """Use range() to iterate over indexes."""
    print("for_with_range:")
    for i in range(len(fruits)):
        print(i, fruits[i])
    print()


def enumerate_example():
    """Use enumerate to get index and value."""
    print("enumerate_example:")
    for idx, fruit in enumerate(fruits, start=1):
        print(idx, fruit)
    print()


def while_example():
    """Classic while loop example."""
    print("while_example:")
    i = 0
    while i < len(fruits):
        print(i, fruits[i])
        i += 1
    print()


def nested_loops():
    """Nested loops: produce pairings or repeated actions."""
    print("nested_loops:")
    for i, f in enumerate(fruits):
        for j in range(2):
            print(f"{i}-{j}: {f}")
    print()


def for_else_example():
    """for..else runs else if loop wasn't terminated by break."""
    print("for_else_example:")
    for f in fruits:
        if f == "kiwi":
            print("Found kiwi!")
            break
    else:
        print("No kiwi in fruits")
    print()


def generator_example():
    """Iterate a simple generator to show lazy iteration."""
    print("generator_example:")

    def squares(n):
        for i in range(n):
            yield i * i

    for s in squares(5):
        print(s)
    print()


def list_comp_example():
    """Show a list comprehension as a concise loop alternative."""
    print("list_comp_example:")
    upper = [f.upper() for f in fruits if f != "banana"]
    print(upper)
    print()


if __name__ == "__main__":
    basic_for()
    for_with_range()
    enumerate_example()
    while_example()
    nested_loops()
    for_else_example()
    generator_example()
    list_comp_example()