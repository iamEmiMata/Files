# lambda 

# suma = lambda a, b : a + b
# print(suma(4,3))

def mi_funcion(lambda_func):
    print(lambda_func(4,3))

# mi_funcion(lambda a, b: a + b)

suma = (lambda *args: sum(args))(1, 2, 3, 4)
# print(suma)

(lambda *args: print(args))('luis', 'petra', 'luisa')

