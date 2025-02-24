cadena = input("Introduce una cadena: ")

print("La cadena introducida es: ", cadena)

print("Solo se imprimen caracteres de índice pares. ")
for i in range(0, len(cadena), 2):
    print(cadena[i])