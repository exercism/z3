from z3 import *

def find_production_and_profit(a_hours, b_hours, total_hours, prices):
    # Create Integer Variables
    qa = Int("qa")
    qb = Int("qb")

    # Declare list for constraints to be appended to
    constraints = []

    # Nonnegative quantity constraints
    constraints.append(qa >= 0)
    constraints.append(qb >= 0)

    # Total hours limitations for each productions stage
    for i in range(len(total_hours)):
        constraints.append((RealVal(a_hours[i]) * qa) + (RealVal(b_hours[i]) * qb) <= RealVal(total_hours[i]))
    
    # Run Z3 Optimizer
    opt = Optimize()
    opt.add(constraints)
    opt.maximize((RealVal(prices[0]) * qa) + (RealVal(prices[1]) * qb))
    if opt.check() == sat:
        m = opt.model()
    else:
        raise ArithmeticError()
    
    # Convert quantities to integers and calculate total profit
    qa = m.eval(qa).as_long()
    qb = m.eval(qb).as_long()
    total_profit = (prices[0] * qa) + (prices[1] * qb)

    return qa, qb, total_profit