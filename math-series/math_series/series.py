series_backtrace = []

def fibonacci(n):
    fibs = [-1] * (n + 1)
    return fibonacci_helper(n, fibs)

def fibonacci_helper(n, fibs):
    if fibs[n] >= 0:
        return fibs[n]
    elif n == 0 or n == 1:
        res = n
    else:
        res = fibonacci_helper(n - 1, fibs) + fibonacci_helper(n - 2, fibs)
    fibs[n] = res
    return res

def lucas(n):
    lucs = [-1] * (n + 1)
    return lucas_helper(n, lucs)

def lucas_helper(n, lucs):
    if lucs[n] >= 0:
        return lucs[n]
    if n == 0:
        res = 2
    elif n == 1:
        res = 1
    else:
        res = lucas_helper(n - 1, lucs) + lucas_helper(n - 2, lucs)
    lucs[n] = res
    return res

def sum_series(n, first=0, second=1):
    series = [-1] * (n + 1)
    return series_helper(n, first, second, series)

def series_helper(n, first, second, series):
    if series[n] >= 0:
        return series[n]
    if n == 0:
        res = first
    elif n == 1:
        res = second
    else:
        res = series_helper(n - 1, first, second, series) + series_helper(n - 2, first, second, series)
    series[n] = res
    return res

    
    