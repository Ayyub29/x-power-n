def myPow(x: float, n: int) -> float:
    calc_res = {} # to store power results
    calc_res[1] = x # initial value, multiplication by 1

    # to cater negative power
    is_negative = False 
    if n < 0:
        is_negative = True
        n = -1 * n

    pow_calculated = 0 # how many power we already calculated
    cur_pow = 1 # current power 
    res = 1
    while pow_calculated < n:
        res *= calc_res[cur_pow]
        pow_calculated += cur_pow
        calc_res[pow_calculated] = res
        if pow_calculated * 2 <= n: 
            cur_pow = pow_calculated
        else:
            pow_remaining = n - pow_calculated
            while pow_remaining < cur_pow:
                cur_pow = cur_pow / 2

    if is_negative:
        res = 1 / res

    return res