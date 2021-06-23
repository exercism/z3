from z3 import *

def least_change(coins, target):
    s = Optimize()
    coin_var = []
    equation_1 = IntVal(0)
    equation_2 = IntVal(0)
    min_coins = Int("min_coins")

    # Fill in the solver with the necessary constraints
    for i in range(len(coins)):
        coin_var.append(Int(str(coins[i])))
        s.add(coin_var[i] >= 0)
        equation_1 += coins[i] * coin_var[i]
        equation_2 += coin_var[i]

    s.add(equation_1 == target,
          equation_2 == min_coins,
          min_coins > 0,
          )

    s.minimize(min_coins)

    if s.check() == sat:
        return s.model()
    else:
        return None

if __name__ == "__main__":
    s = least_change([1, 5, 10, 25, 100], 15)
    print(s)
