def calculo_factorial(n):
    if n == 0 or n ==1:
        return 1
    elif n > 1:
        factorial = n * calculo_factorial(n-1) 
    return factorial