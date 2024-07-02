"""
ESCRIBIR UN PROGRAMA QUE CREE UN DICCIONARIO SIMULANDO UNA CESTA DE LA COMPRA. EL PROGRAMA DEBE PREGUNTAR
EL ARTICULO Y SU PRECIO Y AÑADIR EL PAR AL DICCIONARIO, HASTA QUE EL USUARIO DECIDA TERMINAR. DESPUES
SE DEBE MOSTRAR POR PANTALLA LA LISTA DE LA COMPRA Y EL COSTO TOTAL.
"""


cesta_compra = {}

while True:
    # SE PIDE AL USUARIO QUE INGRESE EL ARTICULO
    articulo = input("Ingresa el nombre del artículo (o 'SALIR' para terminar): ")
    
  
    if articulo.lower() == 'salir':
        break    
    precio = float(input(f"Ingresa el precio de '{articulo}': "))
    
    # SE AÑADE EL ARTICULO Y EL PRECIO AL DICCIONARIO
    cesta_compra[articulo] = precio

# SE MUESTRA LA LISTA Y EL COSTO TOTAL
print("\nLista de la compra:")
total = 0
for articulo, precio in cesta_compra.items():
    print(f"{articulo}: ${precio:.2f}")
    total += precio
print(f"\nCosto total: ${total:.2f}")
