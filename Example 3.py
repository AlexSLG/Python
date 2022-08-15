def suma(n):
  if n==0 :
    return n
  else:
    return suma(n-1) + n
#aqui se elige los N primeros numero que se desea sumar
n=int(input("Ingrese un número: "))
print(suma(n))

