def mcd(a, b):
  a = abs(a);
  b = abs(b);
  if (b == 0):
    return a
  else: 
    return mcd(b, a%b);

a= int(input("ingrese el primer numero : "))
b= int(input("Ingrese el segundo numero: "))

print("El mcd entre los 2 numeros es: ", mcd(a,b))