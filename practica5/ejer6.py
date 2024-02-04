def es_repeticion(cadena):
    mitad = int(len(cadena) / 2)
    if mitad != 2:
        return False
    if cadena[mitad:] == cadena[:mitad]:
        return True
    return False


es_palindromo = "abab"
# es_palindromo = "abba"
print("¿Coincide?:", es_repeticion(es_palindromo))