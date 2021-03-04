# Assignment 3: If statement


def number_equalityCheck(a, b, c):
    """if all of the variable are equal or at least 2 are equal True is returned"""
    if (a == b and b == c and a == c) or (a == b or b == int(c) or a == int(c)):
        return True

    else:
        return False  # however if none of the variables are equal False is returned


"""function into() convert variable type from str to int is a string variable is inputted."""
print((number_equalityCheck(6, 88, 88)))
