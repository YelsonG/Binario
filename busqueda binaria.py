def busqueda_binaria(arr, elemento_buscado):
    inicio = 0
    inicio = 0
    fin = len(arr) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 
        medio = (inicio + fin)
 # Índice medio del rango actual

        if arr[medio] == elemento_buscado:  # Elemento encontrado
            
           
return medio

        elif arr[medio] < elemento_buscado:  # Buscar en la mitad derecha del rango
            inicio = medio + 1

        

       
else:  # Buscar en la mitad izquierda del rango
            fin = medio - 1

    # Elemento no encontrado
    return -1

# Ejemplo de uso:
lista_ordenada = [
lista_ordenada =

lista_

lista
2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
elemento_a_buscar = 
elemento_a_buscar = 
23

indice_encontrado = busqueda_binaria(lista_ordenada, elemento_a_buscar)


indice_encontrado = busqueda_binaria(lista_ordenada, elemento_a_buscar


indice_encontrado = busqueda_binaria(lista_ordenada, elemento


indice_encontrado = busqueda_binaria


indice_encontrado
if indice_encontrado != -1:
    
   
print(f"El elemento {elemento_a_buscar} se encuentra en el índice {indice_encontrado}.")
else:
    
   
print(f"El elemento {elemento_a_buscar} no está presente en la lista.")
