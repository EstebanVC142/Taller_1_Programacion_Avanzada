# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:32:39 2023

@author: Equipo # 4
"""


def euler_method(f, x0, y0, h, num_pasos):
    ##esta funcion recibe los datos iniciales de x & y, tambien el tamaño de paso y numero de pasos
    ##recibe la ecuacion ya evaluada con eval() para luego crear la tabla con un ciclo for y utilizando la operacion matematica vista en el video
    x = x0
    y = y0
    print('\n-------------SOLUCION-------------')
    print('----------------------------------')    
    print('ITERACION \t     X\t\t     Y')
    print('----------------------------------------')
   
    for i in range(num_pasos):
        x_new= x
        y_new = y
        
        print(f" {i}\t\t    {x_new:.2f}\t   {y_new: .6f}")
        x_new = x + h
        y_new = y + h * f(x, y)
        x = x_new
        y = y_new
    
print("solucion de una ecuacion diferencial ordinaria de primer orden por metodo de euler")
# Ingresar las condiciones iniciales, tamaño del paso y número de pasos
x0 = float(input("Ingrese el valor inicial de x: "))
y0 = float(input("Ingrese el valor inicial de y: "))
h = float(input("Ingrese el tamaño del paso (h): "))
n = int(input("Ingrese el número de pasos: "))
##entramos a un ciclo while para pedir al usuario la ecuacion y procedemos a evaluarla, utilizando un if-else
##mientras no se cumpla la condicion seguira pidiendo la ecuacion en terminos de x & y, asegurando las variables para luego evaluarlas
while True:
    ecuacion = input("Ingrese la ecuación en términos de x & y  ")
    
    if 'x' not in ecuacion or 'y' not in ecuacion:
        print("La ecuación debe contener tanto x como y.")
    else: break
resultado = ecuacion

def evaluar_ecuacion(x, y):
    ##esta funcion evalua la ecuacion ya validada anteriormente y la inicializa en los terminos de x & y ya pedidos
    return eval(resultado)

# Resolver la EDO usando el método de Euler
euler_method(evaluar_ecuacion, x0, y0, h, n)