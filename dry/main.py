from environment import Environment

"""
El principio DRY nos indica que debemos evitar a toda costa la repeticion de codigo:
en este caso se extrajo la variable "iva" para ser reutilizadas en la funciones de calcular 
precio final de un articulo, ademas de que si en algun momento el precio del iva
llegase a cambair como esta variable se encuentra en una calse bastaria con 
cambiar el valor de esta para que en todo el codigo se refleje este cambio.
"""


iva = Environment().get_iva()

def calcular_precio_final(precio):

    return precio + (precio*iva)

def calcular_total_final(precios):
    total=0
    for i in precios:
        total = total + calcular_precio_final(i)

    return total

def main():
    precios = [2000,40900,5000,8000]
    print("El total es igual a: ",calcular_total_final(precios))

main()

    






    
