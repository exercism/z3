from z3 import*

def average(x, y):
    z = Real('z')
    s = Solver()
    s.add(z == (x + y)/2)

    print(s.check())
    print(s.model())

    return(s.model().eval(z))
    pass