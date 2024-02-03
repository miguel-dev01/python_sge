def letra_nif(nif):
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    letter = letters[nif % 23]

    return letter


try:
    nif_without_letter = int(input("Introduce nif para averiguar su letra: "))
    print(f"La letra del nif {nif_without_letter} introducido es: {letra_nif(nif_without_letter)}")
except ValueError:
    print("Solo se permiten valores numéricos\nIntentelo de nuevo")