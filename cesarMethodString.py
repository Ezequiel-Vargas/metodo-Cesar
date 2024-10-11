def generarNuevoTexto(texto, corrimiento):
    #Diccionario de errores
    acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'ñ': 'n'
    }
    result = []
    for char in texto:
        #Remplazar tildes y ñ
        if char in acentos:
            char = acentos[char]
        if char.isalpha():
            #Convertir la letra a minúsculas
            base = ord('a')
            #Corrmiento
            new_char = chr((ord(char) - base + corrimiento) % 26 + base)
            result.append(new_char)
        else:
            #Los caracteres que no sean letras pasan igual
            result.append(char)  
    return ''.join(result)

def main():
    archivoEntrada = input("Ingrese el nombre del archivo de texto a procesar (ejemplo: miArchivo.txt):")
    
    try:
        with open(archivoEntrada, 'r', encoding='utf-8') as file:
            texto = file.read().lower()  # Leer el archivo y convertir a minúsculas
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return

    action = input("¿Desea cifrar o descifrar el mensaje? (c/d): ").strip().lower()
    if action not in ['c', 'd']:
        print("Acción no válida. Intente de nuevo por favor.")
        return

    corrimiento = int(input("Ingrese el número de corrimiento (número entero negativo o positivo): "))

    #Para desencriptar
    if action == 'd':
        corrimiento = -corrimiento

    #Llamada a la función 
    textoProcesado = generarNuevoTexto(texto, corrimiento)

    #Crear un nuevo archivo para el texto generado
    salida = input("Ingrese un nombre para guardar el nuevo archivo: ")
    with open(salida, 'w', encoding='utf-8') as file:
        file.write(textoProcesado)

    print(f"El texto ha sido procesado y guardado en '{salida}'.")

if __name__ == "__main__":
    main()
