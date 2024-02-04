dias_mes = int(input("Número de días del mes: "))
primer_dia_semana = int(input("Día 1 es (0 lunes, 6 domingo): "))

dias_semana = ['L', 'M', 'X', 'J', 'V', 'S', 'D']

for dia in dias_semana:
    print(dia, end="\t")

dia_iterable = 0
print()
for i in range(5):
    for j in range(7):
        if dia_iterable > dias_mes:
            break
        if j < primer_dia_semana and i == 0:
            print("", end="\t")
        else:
            dia_iterable += 1
            print(dia_iterable, end="\t")
    print()