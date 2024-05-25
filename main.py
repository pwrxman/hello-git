
print("Hello Dear Git")
# xname = "John"
# xage = "35"
# print("Hello "+ xname+ ",")
# print("your age is " + xage + "!!")
# print(xname.upper())
# print("My name is {0}".format(xname))
# print(f"Mi nombre es {xname}")

# # NUMBERS

# print(7 / 7)
# print(4%7)
# print(100/5)
# print(100//5)

# age = input("Dime edad: ")
# print("el tipo de age " + age +" es ", type(age))


#LISTAS
# estru = [1, "perro", 6, 1.14, [1,2,3,4]]
# colors = ["red", "green", "red"]

# #usando el constructor list
# number_list = list((1,2,3,4,5))
# print(type(number_list))

# r = range(1,101)  #crea unalista de 100 elementos , del 1 al 100 (1 menos del 2o parametro)
# print(dir(colors))  #despliega lista de metodos
# print(len(colors))  # lista de numero de elementos
# print(estru[4])  
# print('green' in colors)  #para saber si un elemento pertenece a una lista  
# print(estru[-4])  # muesstra elemento en cuarto lugar contando de atras para adelante
# colors.append('violet')
# print(colors)
# colors.extend(['yellow', 'blue'])   #insertar mas de un elemento utilzando una tupla
# print(colors)
# colors.insert(2, 'purple')
# print(colors)   #'red', 'green', 'purple', 'red', 'violet', 'yellow', 'blue']
# colors.insert(-2, 'violet')
# print(colors)   #['red', 'green', 'purple', 'red', 'violet', 'violet', 'yellow', 'blue']
# colors.pop()  # remueve el utltimo elemento
# print(colors)   #['red', 'green', 'purple', 'red', 'violet', 'violet', 'yellow']
# colors.pop(2)  # remueve el elemento 2
# print(colors)   #'red', 'green', 'red', 'violet', 'violet', 'yellow']
# colors.remove('green')  # remueve el elemento con valor green
# print(colors) 
# colors.sort()
# colors.sort(reverse=True)


#TUPLAS
# las tuplas son como listas pero cuyos valores no se pueden cambiar

# x = (1, 2, 3, 4)
# print(x)
# print(type(x))
# # (1, 2, 3, 4)
# # <class 'tuple'>

# #tambien tienen su constructor
# x1 = tuple((9, 8, 7, 6, 5))
# print(x1)
# print(type(x1))
# print(dir(x1))  # muestra todos los metodos que aplican para una tupla
# #(9, 8, 7, 6, 5)
# #<class 'tuple'>
# #['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

# print(x1[3])
#6

#SET
# son colecciones que no tienen indices
# x = {'r', 'b', 'g'}
# print(type(x))
# print(x)
# print(dir(x))
# print('b' in x)
# x.add('v')
# print(x)
# x.remove('r')
# print(x)
# x.clear()  #vacia el contenido de un set
# print(x)
# del x  #elimina el set x
#<class 'set'>
#{'r', 'b', 'g'}
#['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
#True
#{'v', 'g', 'b'}
#set()

#DICCIONARIO
# x = { 
#     'name': "Book",
#     'cantidad': 3,
#     "precio": 4.99
#     }
# print(type(x))
# print(x)
# print(dir(x))
# print(x.keys())
# print(x.items())
# x.clear()
# print(x)
# print("LISTA QUE CONTIENE UN DICCIONARIO")
# products = [
#     {"name":  'book', "price": 10.99},
#     {"name":  'Laptop', "price": 2999}
# ]
# print(products)

# <class 'dict'>
# {'name': 'Book', 'cantidad': 3, 'precio': 4.99}
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
#dict_keys(['name', 'cantidad', 'precio'])
#dict_items([('name', 'Book'), ('cantidad', 3), ('precio', 4.99)])
#{}
#LISTA QUE CONTIENE UN DICCIONARIO
#[{'name': 'book', 'price': 10.99}, {'name': 'Laptop', 'price': 2999}]



#CONDITIONALS

# x = 30
# if x > 30:
#     print('x es menor que 30')
# elif x == 30:
#     print("x es igual  a 30")    
# else:
#     print("x es mayor o igual que 30")

# #Operadores logicos

# x = 6
# if x > 2 and x < 10:
#     print("x esta entre 2 y 10")

# if x > 2 or x < 20:
#     print("x es mayor a 2 O x es menor que 20")

# if not(x==6):
#     print("x no es igual a 6")

# #BUCLES

# foods = ['manzana', 'pina', 'uva', 'melon']    
# for food in foods:
#     if food == 'uva':
#         print('tienes que comprar uvas')
#         break
#     if food == 'pina':
#         print('no olvodes pina')
#         continue
#     print(food)

# count = 0
# for letter in 'Snow!':
#   print('Letter # ' + str(count) + ' is ' + str(letter))
#     count += 1
#     break
# print(count) 

# num = 10
# for num in range(5):
#     print(num)
# print(num)

# iteration = 0
# count = 0
# while iteration < 5:
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# s = 'azcbobobegghakl'
# numvoc = 0
# for i in s:
#      if i in ("aeiou"):
#           numvoc += 1

# print(numvoc)

# s = "abcdefgh"
# s[::-1]
# BHD54504AMA

# for letra in "Hello":
#     print(letra)

# count = 4
# while count <= 10:
#     print(count)
#     count = count + 1

# x es igual  a 30
# x esta entre 2 y 10
# x es mayor a 2 O x es menor que 20
# manzana
# no olvodes pina
# tienes que comprar uvas
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# H
# e
# l
# l
# o
# 4
# 5
# 6
# 7
# 8
# 9
# 10


#FUNCIONES
# def hello():
#     print("Hello World")

# hello()


# def hellop(name = 'Person'):
#     print("Hello ", name)

# hellop("Andy")
# hellop("Rose")
# hellop("darling")
# hellop()  # al no pasar argumentos se asigna el valor por default asignado en la definicion de la funcion
# Hello World
# Hello  Andy
# Hello  Rose
# Hello  darling
# Hello  Person

# def suma(n1, n2):
#     return n1 + n2

# print(suma(5, 11))    

# sumal = lambda n1, n2: n1 + n2
# print(sumal(10, 20))

#MODULOS

#own modules
#ptyhon modulos
# third poarty modules

#Lista de modulos de python en internet buscar "Python modules list" o bien docs.python.org
# Lista de modulos de terceros pypi.org

# import datetime

# print(datetime.date.today())
# print(datetime.timedelta(minutes=70))
#2021-01-22
#1:10:00

#otra forma alternativa de hacer los import es como sigue

# from datetime import date, timedelta
# print(timedelta(minutes=70))
# print(date.today())
# # 1:10:00
# # 2021-01-22

# #para definir un modulo personal hay que crear el archivo correspondienter que contenga las funciones necesarias, en ste caso ejemplificaremois coin un  archivo llamado madd.py

# import madd

# madd.myadd(10, 27)
# madd.mysubs(54, 23)

# from madd import mymult
# mymult(20, 5)

# # PARA INSTALAR MODULOS DE TERCEROS DESDE INTERNET.
# #1. DESCARGARLOS DE pypi.org
# #2. EJECUTAR EN EL EQUIPO pip install colorama    colorama es en un ejemplo
# # se importa al codigo con import colorama 
# # o bien con from colorama import Fore, Style
# # ver ejemplo en la documen tacion de colorama en pypi.org



# from colorama import Fore, Style, init
# init(convert=True)
# print(Fore.RED + "Hello World")


#hay otros modulos que son frameworks, como FLASK o DJANGO. TKINTER