def longitud_collatz(n):
    pasos = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pasos += 1
    return pasos

mejor_numero = 0
max_terminos = 0

for i in range(1, 1000000):
    terminos = longitud_collatz(i)
    if terminos > max_terminos:
        max_terminos = terminos
        mejor_numero = i


print(f"Número inicial con cadena más larga: {mejor_numero}")
print(f"Cantidad de términos: {max_terminos}")