dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dia_semana = 0
domingos = 0

for año in range(1900, 2001):
    es_bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

    for mes in range(12):
        if año >= 1901 and dia_semana == 6:
            domingos += 1

        dias_actuales = dias_mes[mes]
        if mes == 1 and es_bisiesto:
            dias_actuales = 29

        dia_semana = (dia_semana + dias_actuales) % 7

print(domingos)