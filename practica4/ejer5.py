cantidad = int(input("Introduce cantidad a desglosar: "))
result = {500: 0,
          200: 0,
          100: 0,
          50: 0,
          20: 0,
          10: 0,
          5: 0,
          2: 0,
          1: 0}

for i in result:
    result[i] = cantidad / i
    cantidad = cantidad % i

for clave, valor in result.items():
    dinero_fisico = "billetes"
    if int(valor) == 1 and clave <= 2:
        dinero_fisico = "moneda"
    elif clave <= 2:
        dinero_fisico = "monedas"
    elif int(valor) == 1 and clave >= 3:
        dinero_fisico = "billete"

    if int(valor) != 0:
        print("De", clave, "hace falta", int(valor), dinero_fisico)