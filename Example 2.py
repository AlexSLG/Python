def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)
n= int(input("ingrese el numero: "))
print(fib(n))