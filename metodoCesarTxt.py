def generarNuevoTexto(texto, corrimiento):
    # Diccionario de errores
    acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'ñ': 'n'
    }
    result = []
    for char in texto:
        #Reemplazar tildes y ñ
        if char in acentos:
            char = acentos[char]
        if char.isalpha():
            #Convertir la letra a minúsculas
            base = ord('a')
            #Corrimiento
            nuevocaracter = chr((ord(char) - base + corrimiento) % 26 + base)
            result.append(nuevocaracter)
        else:
            #Los caracteres que no sean letras pasan igual
            result.append(char)
    return ''.join(result)

def encriptar(texto, corrimiento):
    return generarNuevoTexto(texto.lower(), corrimiento)

def desencriptar(texto, corrimiento):
    return generarNuevoTexto(texto.lower(), -corrimiento)

def main():
    texto = input("Ingresa el texto a procesar: ")
    accion = input("¿Desea cifrar o descifrar el mensaje? (c/d): ").strip().lower()
    
    if accion not in ['c', 'd']:
        print("Acción no válida. Intente de nuevo por favor.")
        return

    corrimiento = int(input("Ingresa el número de corrimiento (número entero negativo o positivo): "))

    #Llamada a la función correspondiente
    if accion == 'c':
        textoProcesado = encriptar(texto, corrimiento)
        print(f"Texto cifrado: {textoProcesado}")
    else:
        textoProcesado = desencriptar(texto, corrimiento)
        print(f"Texto descifrado: {textoProcesado}")

if __name__ == "__main__":
    main()
