def fib(num):
    fibn = [0, 1]
    i = 2
    while (i <= num):
        var = fibn[i - 1] + fibn[i - 2]
        fibn.append(var)
        i = i + 1 
    return fibn

resultado = fib(num)
print(resultado)