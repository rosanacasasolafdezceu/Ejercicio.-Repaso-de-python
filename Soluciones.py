import re
import random

#  Ejercicio 1: Decodificador de Mensajes Secretos
def decodificar_mensaje(mensaje):
    mensaje_volteado = mensaje[::-1]
    mensaje_limpio = re.sub(r'[^a-zA-Z]', '', mensaje_volteado)
    print("Mensaje limpio:", mensaje_limpio)
    return mensaje_limpio

#  Ejercicio 2: Simulador de Ahorro Mensual
def simulador_ahorro(cantidad_inicial, cantidad_mensual, meses):
    total = cantidad_inicial + cantidad_mensual * meses
    print("Total ahorrado:", total)
    if total > 5000:
        print("¡Felicidades! Has superado los 5000€ de ahorro.")
    return total

#  Ejercicio 3: Clasificador de Números
def clasificar_numeros(lista):
    pares = []
    impares = []
    negativos = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
        if num < 0:
            negativos.append(num)
    return pares, impares, negativos

#  Ejercicio 4: Calculadora de Notas
def calculadora_notas(notas):
    media = sum(notas) / len(notas) if notas else 0
    nota_max = max(notas) if notas else None
    nota_min = min(notas) if notas else None
    print(f"Media: {media:.2f}")
    print(f"Nota más alta: {nota_max}")
    print(f"Nota más baja: {nota_min}")
    if any(n < 5 for n in notas):
        print("Hay alguna nota suspensa (<5).")
    return media, nota_max, nota_min

#  Ejercicio 5: Generador de ADN
def generar_adn(n):
    bases = ['A', 'T', 'C', 'G']
    cadena = ''.join(random.choice(bases) for _ in range(n))
    conteo = {base: cadena.count(base) for base in bases}
    print("Cadena de ADN:", cadena)
    print("Conteo:", conteo)
    return cadena, conteo

#  Ejercicio 6: Inventario de Personajes
def inventario_personajes(diccionario):
    humanos = sorted([nombre for nombre, tipo in diccionario.items() if tipo == "humano"])
    criaturas = sorted([nombre for nombre, tipo in diccionario.items() if tipo == "criatura"], key=len)
    print("Humanos ordenados:", humanos)
    print("Criaturas ordenadas por longitud:", criaturas)
    return humanos, criaturas

#  Ejercicio 7: Analizador de URL
def analizar_url(url):
    try:
        protocolo = None
        dominio = None
        recurso = None
        if '://' in url:
            protocolo, resto = url.split('://', 1)
        else:
            resto = url
        partes = resto.split('/', 1)
        dominio = partes[0]
        recurso = partes[1] if len(partes) > 1 else None
        print("Protocolo:", protocolo)
        print("Dominio:", dominio)
        print("Recurso:", recurso)
        return protocolo, dominio, recurso
    except Exception as e:
        print("Error al analizar la URL:", e)
        return None, None, None