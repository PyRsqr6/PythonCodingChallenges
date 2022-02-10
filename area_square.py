#write a unit test for function area of a square
def area_square(s):
    if type(s) not in [int,float]:
        raise TypeError("Square dimensions must be non negative real numbers")
    if s < 0:
        raise ValueError("Square dimensions cannot be negative")
    return s**2
