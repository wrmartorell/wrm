# Versión 2 — sin frecuencia + reset del domingo

Código: `src/v2.py`. La V1 no se modificó.

## Por qué

La V1 con historia completa repetía casi siempre los mismos dígitos (4 en el Top 4 27/27, 5 24/27, 8 23/27): eran los más frecuentes. El conteo de "qué sale después de X" terminaba siendo frecuencia.

## Cambios aprobados

1. **Efecto en vez de conteo:** efecto(y|x) = P(y en el siguiente | x presente) − P(y en el siguiente). S(y) = promedio sobre los dígitos distintos del último resultado.
2. **Reset del domingo en el motor:** martes→sábado usan solo transiciones dentro de la semana; los lunes usan solo transiciones sábado→lunes.

Igual que V1: repetidos una vez, desempate dígito menor, historia completa, vertical y combinado 37.1.

## Resultados (fecha por fecha, solo datos anteriores)

| Bloque | Versión | ≥2 | ≥3 | Todos | Aciertos |
|---|---|---|---|---|---|
| Aprendizaje 15/08–29/08 (13) | V1 | 9/13 | 2/13 | 0/13 | 24 |
| | V2 | 6/13 | 1/13 | 0/13 | 20 |
| Reserva 31/08–30/09 (27) | V1 | 18/27 | 7/27 | 4/27 | 52 |
| | **V2** | **22/27** | **10/27** | **5/27** | **60** |

Reales por posición en la reserva (#1..#10):
- V1: 12 11 9 8 12 8 10 8 9 9 (casi plano)
- V2: 16 9 11 14 10 8 7 10 5 6 (el #1 acierta 16/27; Top 5 = 60, Bottom 5 = 36)

Dígitos más repetidos en el Top 4 (reserva): V1 4(27) 5(24) 8(23); V2 5(16) 0(14) 4(13) 8(13) 2(13). El ranking ya no es fijo.

## Lectura

- En la reserva, V2 supera a V1 en todas las medidas y el ranking tiene más orden (#1 real 59% de las veces).
- En aprendizaje fue peor: en agosto había muy poca historia (pocas transiciones, sobre todo sábado→lunes).
- Las 27 fechas de la reserva ya se habían visto; V2 no se ajustó a ellas (salió del principio "sin frecuencia + reset"), pero la prueba real es el 1 de octubre y las fechas nuevas.

## Estado

V2 en prueba. Salida del 1 de octubre congelada en `docs/predicciones/2026-10-01.md` antes de conocer el resultado.
