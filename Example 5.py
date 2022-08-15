def binario(n):
    if n == 0:
        return ""
    else:
        return binario(n//2)+ str(n % 2)
n=int(input("Ingrese el número que quiere convertir a binario: "))
print(binario(n))