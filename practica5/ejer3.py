def es_nif(nif):
    if len(nif) != 9 and type(nif[:-1]) != int:
        return False

    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    letter = letters[int(nif[:-1]) % 23]

    if nif[-1:] == letter or nif[-1:] == letter.lower():
        return True
    return False

nif = str(input("Introduce un nif: "))

if es_nif(nif):
    print("El nif es correcto")
else:
    print("El nif es incorrecto")
