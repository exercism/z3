from z3 import *

def generate_third_points(first_point, second_point):

    # TODO: Write your code here

    pass

# Do not modify this function!
# Works as described below
def convert_to_float(z3_number):
    """ 
    Converts AlgebraicNumRef, IntNumRef, and RatNumRef
    to a float from its string representation
    """

    # Get the Z3 Number's string representation
    z3_number_string = str(z3_number)

    # Remove ? from long decimal number if necessary
    z3_number_string = z3_number_string.rstrip('?')

    # Convert remaining string to a float
    z3_number_float = float(z3_number_string)

    return z3_number_float