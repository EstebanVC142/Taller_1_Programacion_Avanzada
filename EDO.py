# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:32:39 2023

@author: Equipo # 4
= Santiango Salazar Avendano
= Sebastian Rios Roman
= Esteban Vásquez Cano
"""

def euler_method(f, x0=0, y0=0, tamaño_paso=0.1, numero_pasos=10):
# =============================================================================
#     Esta función recibe los datos iniciales de x & y, también el tamaño de paso y número de pasos,
#     también recibe la ecuacion evaluada con eval() para luego crear y llenar la tabla con un ciclo for y 
#     utilizando la operacion matematica vista en el video
# =============================================================================
    x = x0
    y = y0
    print('\n', '='*13,'SOLUCIÓN', '='*13)
    print('='*40)    
    print(' ITERACIÓN \t|    X\t |\t   Y')
    print('='*40)
   
    for paso in range(numero_pasos + 1):
        x_new= x
        y_new = y
        
        print(f" \t{[paso]}\t\t|  {x_new:.2f}\t |  {y_new: .4f}")
        x_new = x + tamaño_paso
        y_new = y + tamaño_paso * f(x, y)
        x = x_new
        y = y_new
        
def evaluar_ecuacion(x, y):
# =============================================================================
#     Esta función evalua la ecuacion ya validada anteriormente y la inicializa en los terminos de x & y 
#     ya pedidos
# =============================================================================
    return eval(resultado)
    
print("\nEste script soluciona una ecuación diferencial ordinaria de primer orden por el método de Euler.\n")
# Ingresar las condiciones iniciales, tamaño del paso y número de pasos
# x0 = float(input("Ingrese el valor de la condición inicial de x: "))
# y0 = float(input("Ingrese el valor de la condición inicial de y: "))
# tamaño_paso = float(input("Ingrese el tamaño del paso: "))
# numero_pasos = int(input("Ingrese el número de pasos: "))
# =============================================================================
# Entramos a un ciclo While() para pedir al usuario la ecuación y procedemos a evaluarla, utilizando un if-else
# mientras no se cumpla la condicion seguira pidiendo la ecuación en terminos de x & y, asegurando las 
# variables para luego evaluarlas
# =============================================================================
while True:
    ecuacion = input("Ingrese la ecuación en términos de x & y: ")
    
    if 'x' not in ecuacion or 'y' not in ecuacion:
        print("La ecuación debe contener tanto x como y.\n")
    else: break
resultado = ecuacion

# Resolver la EDO usando el método de Euler
euler_method(evaluar_ecuacion)