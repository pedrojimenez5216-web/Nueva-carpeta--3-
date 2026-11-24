# Contador de domingos en primer día de mes (Siglo XX)

Código en Python para calcular cuántos domingos cayeron en día 1 de mes del 1 de enero de 1901 al 31 de diciembre de 2000, partiendo de que el 1 de enero de 1900 fue lunes.

## Cómo funciona

1. Se define la duración base de cada mes en una lista y se inicia `dia_semana = 0` (representando lunes = `0` hasta domingo = `6`).
2. Se recorren los años desde `1900` hasta `2000` para avanzar el calendario desde la fecha inicial conocida y detectar años bisiestos.
3. En cada año se recorren los 12 meses:
   - Si el año es mayor o igual a `1901` y `dia_semana == 6` (domingo), se suma `1` al contador.
   - Si el mes es febrero (`mes == 1`) y el año es bisiesto, se usan `29` días en lugar de `28`.
   - Se actualiza `dia_semana` sumando los días del mes actual y aplicando módulo `7` (`% 7`).
4. Al finalizar el recorrido, se imprime el total de domingos encontrados.

## Ejecución

```bash
python mrd.py