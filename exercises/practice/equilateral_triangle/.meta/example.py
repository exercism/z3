from z3 import *

def generate_third_points(first_point, second_point):
    # Constants to determine x and y indices of input points
    X_INDEX = 0
    Y_INDEX = 1

    # Create Z3 Variables
    # x and y coordinates of points
    x = [Real(f"x{i}") for i in range(3)]
    y = [Real(f"y{i}") for i in range(3)]
    # Triangle side length
    l = Real("l") 

    # Assign first and second coordinates to their corresponding z3 variables
    constants = [
        x[0] == first_point[X_INDEX],
        y[0] == first_point[Y_INDEX],
        x[1] == second_point[X_INDEX],
        y[1] == second_point[Y_INDEX],
    ]

    # Create distance equations in z3
    # All points should be the same distance from each other
    distance_equations = []
    for i in range(3):
        index = i
        index2 = (i + 1) % 3
        distance_equations.append(l**2 == (x[index2] - x[i]) ** 2 + (y[index2] - y[index]) ** 2)

    # Equation that can decide which of the two points to determine
    point_decider_equation1 = If(y[1] != y[0], x[2] > ((x[1] + x[0]) / 2), y[2] > y[0])
    point_decider_equation2 = If(y[1] != y[0], x[2] < ((x[1] + x[0]) / 2), y[2] < y[0])

    # Create solver with constants and distance equations as constraints
    solver = Solver()
    solver.add(constants + distance_equations)

    # Use first point decider equation to find first point
    solver.push()
    solver.add(point_decider_equation1)
    if solver.check() == sat:
        model = solver.model()
        x2 = convert_to_float(model.eval(x[2]))
        y2 = convert_to_float(model.eval(y[2]))
        third_point_1 = x2, y2
    else:
        raise ArithmeticError("Equations not satisfiable for first point")
    solver.pop()

    # Use second point decider equation to find second point
    solver.push()
    solver.add(point_decider_equation2)
    if solver.check() == sat:
        model = solver.model()
        x2 = convert_to_float(model.eval(x[2]))
        y2 = convert_to_float(model.eval(y[2]))
        third_point_2 = x2, y2
    else:
        raise ArithmeticError("Equations not satisfiable for second point")
    solver.pop()

    return third_point_1, third_point_2

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
