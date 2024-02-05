#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer with "{:d}".format().
    Args: value (int): The integer to print.

    Returns: True if no error at all
            otherwise if a TypeError or ValueError occurs - False
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
