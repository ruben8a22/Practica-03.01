#Escribir dos funciones, una función que reciba un número entero positivo n y calcule el número de fibonacci asociado
# a ese número de manera recursiva y otra función que haga la misma operación pero con bucles.
#Con ambas funciones, calcular y comparar el tiempo de ejecución para n = (1, 10, 20, 30 y 40) por fuerza bruta.
import datetime


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 30

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


def fibBuc(n):
    a = 0
    b = 1

    for k in range(n):
        c = b + a
        a = b
        b = c

    return a

start_time = datetime.datetime.now()
#print(fibRec(40))

print(recur_fibo(40))
end_time = datetime.datetime.now()
print(end_time - start_time)

