# Instructions

There are two different types of motors a single manufacturer can produce; the motors
will be called motor A and motor B from this point forward.  Both motors have 3 components
required for production: wiring, drilling, and assembly.  Each motor has a different amount
of time required for each of these stages in production.  Generally, a single unit of motor A
requires t_a_1 hours for wiring, t_a_2 hours for drilling, and t_a_3 hours for assembly.  On
the other hand, a single unit of motor B requires t_b_1 hours for wiring, t_b_2 hours for
drilling, and t_b_3 hours for assembly.  Implement a function that when given the total amount
of hours allocated for each stage of production (t_1 hours for wiring, t_2 hours for drilling,
and t_3 hours for assembly) and the prices for each type of motor (p_a, p_b), compute the optimal 
quantities of motor A and motor B that maximizes profit.

The function will have 4 total input parameters.  They are described below:
1. a_hours: three-tuple of (t_a_1, t_a_2, t_a_3) in hours
2. b_hours: three-tuple of (t_b_1, t_b_2, t_b_3) in hours
3. total_hours: three-tuple of (t_1, t_2, t_3) in hours
4. prices: two-tuple of (p_a, p_b) in dollars

The output should be a single three-tuple consisting of (q_a, q_b, profit) where:
1. q_a: optimal quantity of motor A to produce
2. q_b: optimal quantity of motor B to produce
3. profit: maximizing profit value in dollars

Other important points to note:
q_a and q_b cannot be floating-points numbers because a fraction of a motor cannot be produced.
The Z3 model results for variables will need to be converted to ints before being output.  If the Z3
model result is of type `IntNumRef`, the `as_long()` class method may be used to convert to an integer.