def fib_iter(n):
   if(n == 0):
       return 0
   if(n == 1):
       return 1
   fib_anterior_anterior = 0
   fib_anterior = 1
   fib_nuevo = 0
   for i in range(2, n+1):
       fib_nuevo = fib_anterior + fib_anterior_anterior
       fib_anterior_anterior = fib_anterior
       fib_anterior = fib_nuevo
   return fib_nuevo
print(fib_iter(1000000))