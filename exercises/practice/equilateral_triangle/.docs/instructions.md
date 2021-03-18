# Instructions

Use Z3 to implement a function that, when given two points on the 2D coordinate 
plane, produces a third point such that the connection of these points
results in an equilateral triangle.  However, two points should be output
because there are two possible "third" points to produce an equilateral triangle.
It is worth noting that an equilateral triangle is defined as a three-sided shape 
in which all three sides have equal length.

The function inputs two python tuples, each specifying the x and y coordinates of
each point, as floats.  For example, (0.0, 0.0) and (1.0, 1.0) could be inputs.

The function should output a tuple that consists of two tuples, each specifying
the x and y coordinates of each point, as floats.  For example, ((0.0, 0.0), (1.0, 1.0)) 
could be a potential output.

The function should raise an ArithmeticError built-in python exception if
Z3 solver produces a result that is not satisfiable.  An ArithmeticError 
should also be raised if both input points are the same.

Since the model interpretation of a Z3 Real variable is an instance of
AlgebraicNumRef, IntNumRef, or RatNumRef, a function is provided to convert
this instance to a float.

