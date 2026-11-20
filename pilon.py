def longitud_collatz(n):
    pasos = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pasos += 1
    return pasos


print("Prueba con 13:", longitud_collatz(13))

mejor_numero = 0
max_terminos = 0

for inicio in range(1, 1_000_000):
    terminos = longitud_collatz(inicio)
    if terminos > max_terminos:
        max_terminos = terminos
        mejor_numero = inicio

print(f"Número inicial con cadena más larga: {mejor_numero}")
print(f"Cantidad de términos: {max_terminos}")