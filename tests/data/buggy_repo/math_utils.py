def calculate_average(numbers):
    # Bug: Should divide by len(numbers), but incorrectly uses a hardcoded value or has a logic error.
    # We'll make it return a wrong value.
    if not numbers:
        return 0
    return sum(numbers) / (len(numbers) + 1) # BUG: +1
