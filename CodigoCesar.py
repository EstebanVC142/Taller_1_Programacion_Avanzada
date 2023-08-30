# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:32:39 2023

@author: Esteban VC
"""

def codificar_mensaje(mensaje, desplazamiento=3):
    mensaje_codificado = ""
    
    for letra in mensaje:
        if letra.isalpha(): # Verificar que sea letra
            
            es_mayuscula = letra.isupper() # Determinar si es mayúscula o minúscula
            letra = letra.lower()  # Convertir a minúscula para cálculos internos
            
            # Aplicar el cifrado solo a letras del alfabeto
            letra_codificada = chr(((ord(letra) - ord('a') + desplazamiento) % 26) + ord('a'))
            
            # Convertir de nuevo a mayúscula si era mayúscula originalmente
            if es_mayuscula:
                letra_codificada = letra_codificada.upper()
            
            mensaje_codificado += letra_codificada
        else:
            # Mantener caracteres que no son letras sin cambios
            mensaje_codificado += letra
    
    return mensaje_codificado

def decodificar_mensaje(mensaje, desplazamiento=3):
    mensaje_decodificado = ""
    
    for letra in mensaje:
        if letra.isalpha(): # Verificar que sea letra
            
            es_mayuscula = letra.isupper() # Determinar si es mayúscula o minúscula
            letra = letra.lower()  # Convertir a minúscula para cálculos internos
            
            # Aplicar el cifrado solo a letras del alfabeto
            letra_decodificada = chr(((ord(letra) - ord('a') - desplazamiento) % 26) + ord('a'))
            
            # Convertir de nuevo a mayúscula si era mayúscula originalmente
            if es_mayuscula:
                letra_decodificada = letra_decodificada.upper()
            
            mensaje_decodificado += letra_decodificada
        else:
            # Mantener caracteres que no son letras sin cambios
            mensaje_decodificado += letra
    
    return mensaje_decodificado

def ingresar_numero_entero_positivo(mensaje):
    bandera = 0
    while (bandera == 0):
        numero = int(input(mensaje))
        if numero >= 0:
            bandera = 1
        else:
            print( "Digite un numero entero positivo\n")
    return numero

print('Este script codifica o decodifica un mensaje.')
opcion = input('Ingrese | c | si quiere codificar un mensaje o | d | si quiere decodificar: ').lower()
mensaje = input('Ingrese el mensaje a codificar o decodificar: ')
desplazamiento = ingresar_numero_entero_positivo('Ingrese el valor de desplazamiento: ')

if opcion == 'd':
    mensaje_decodificado = decodificar_mensaje(mensaje, desplazamiento)
    print("Mensaje decodificado:", mensaje_decodificado)
elif opcion == 'c':
    mensaje_codificado = codificar_mensaje(mensaje, desplazamiento)
    print("Mensaje codificado:", mensaje_codificado)
else: 
    print('Debe ingresar una opcion valida.')
