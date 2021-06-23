#Instructions
Determine the fewest number of coins to be given to a customer such
that the sum of the coins' value would equal the correct amount of change.

The first parameter for your function is coins, an array of integer coin values.  The second parameter is target, the 
value we want to find the least amount of coins to add up to. 
Your function should return a Z3 model with the variables named after the coin values, and include a variable of the number of coins in the solution as min_coins.

## Examples
- coins = [1, 5, 10, 21, 25] and target = 63 should return a model that looks like [10 = 0, 25 = 0, 21 = 3, 5 = 0, min_coins = 3, 1 = 0].
- coins = [2, 5, 10, 20, 50] and target = 21 should return a model that looks like [10 = 1, 50 = 0, 2 = 3, 20 = 0, 5 = 1, min_coins = 5].