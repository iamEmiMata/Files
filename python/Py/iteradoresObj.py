'''
Iteradores . __iter__() &&   __next__()

Lists, tuples, dictionaries, and sets are all iterable objects. 
They are iterable containers which you can get an iterator from.

All these objects have a iter() method 
which is used to get an iterator:
'''

tupla = ("Andres", "Barbara", "Camila", "Daniel")
iterador = iter(tupla)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))