"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# write down what you think the output of this will be,
# output will return the number of odd number between 0 and n i.e. 3

# use the debugger to step through and see what's actually happening
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return 1   # Break point
    print(n ** 2)
    return do_something(n - 1)

# write down what you think the output of do_something(4) will be,
# no break point. endless recursion loop

# use the debugger to step through and see what's actually happening


do_something(4)


def brick_loop(rows):
    for i in range(0, rows):
        rows += i
    return rows


print(brick_loop(6))


def brick_recursion(rows):
    if rows == 0:
        return 0
    return rows + brick_recursion(rows - 1)


print(brick_recursion(6))
