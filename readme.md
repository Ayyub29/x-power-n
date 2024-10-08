# MyPow Function

## Overview

The `myPow` function is designed to compute the power of a given floating-point number `x` raised to an integer exponent `n`. It handles both positive and negative values of `n` using an optimized approach that reduces the number of multiplications.

## Function Signature

```python
def myPow(x: float, n: int) -> float:
Parameters:
x (float): The base number to be raised to a power.
n (int): The exponent (can be positive, negative, or zero).
Returns:
float: The result of x raised to the power of n.
```

## How it Works
The algorithm uses a dictionary (calc_res) to store intermediate results of power calculations. This avoids recalculating powers repeatedly and speeds up the process.

## Key Features:
Optimized Power Calculation:
The function reduces unnecessary multiplications by storing results for powers that have already been calculated.
It uses a combination of doubling and halving strategies to efficiently calculate powers, making it faster than a naive multiplication loop.
Handles Negative Powers:
If the exponent n is negative, the function calculates the positive exponent first and then returns its reciprocal.
Edge Cases
If n = 0, the function will return 1 since any number raised to the power of 0 is 1.
If n < 0, the function calculates x^|n| and then returns 1 / result.

#### Example 1: Positive power
result = myPow(2, 10)
print(result)  # Output: 1024.0

#### Example 2: Negative power
result = myPow(2, -3)
print(result)  # Output: 0.125
Time Complexity
The time complexity of the myPow function is approximately O(log n) due to the halving and doubling strategies, making it more efficient than a linear solution.

