

def increment(input):
    try:
        input_int = int(input)
    except ValueError as e:
        raise ValueError(f"Must supply a valid integer (as a string is acceptable). Traceback: {e}")

    return input_int + 1