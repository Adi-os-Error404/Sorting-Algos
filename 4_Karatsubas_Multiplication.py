
def karatsuba(x, y):

    if x < 10 and y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    if ( n%2 != 0): n-=1
    half_n = n//2

    x_m, x_l = x // (10**half_n), x % (10**half_n)
    y_m, y_l = y // (10**half_n), y % (10**half_n)

    a = karatsuba( x_m, y_m )
    b = karatsuba( x_l, y_l )
    c = karatsuba( x_m+x_l, y_m+y_l )
    z = c-(a+b)

    res = (a*10**n) + (z*10**half_n) + b
    return res


print(karatsuba(124, 4321))