# A/B/C/D integrado — motor antiguo por posición (pregunta 31.2)

Código: `src/abcd.py`. V1 no cambia. Fechas en orden, cada una con solo datos anteriores.

Variantes: "misma" (posición p solo mira el valor anterior de p) y "cruzada" (posición p mira los 4 dígitos anteriores), con historia completa, ventana 12 y 18. Combinadas con el valor vertical de cada posición (análogo a 37.1).
Medida: ¿el valor real de cada posición quedó dentro del Top 3 de esa posición?

## Aprendizaje 15/08 → 29/08 (13 fechas)

Todas las variantes: 12–13 de 52 posiciones en Top 3; casi ninguna fecha con ≥3 posiciones. Ganadora por criterio: misma/completa.

## Reserva 31/08 → 30/09 (27 fechas)

| Variante | ≥3 posiciones en Top 3 | 4 posiciones | Posiciones en Top 3 | Valor #1 exacto |
|---|---|---|---|---|
| **misma/completa (ganadora)** | 1/27 | 0/27 | 31/108 (29%) | 12/108 |
| misma/v12 | 1/27 | 0/27 | 28/108 (26%) | 11/108 |
| misma/v18 | 1/27 | 0/27 | 30/108 (28%) | 16/108 |
| cruzada/completa | 0/27 | 0/27 | 31/108 (29%) | 16/108 |
| cruzada/v12 | 4/27 | 0/27 | 40/108 (37%) | 16/108 |
| cruzada/v18 | 3/27 | 0/27 | 36/108 (33%) | 14/108 |

Vertical sola: valor exacto en 8/108 posiciones.

## Lectura

- Un Top 3 por posición cubre 3 de 10 valores (30%). La ganadora acierta 29%: por posición, este motor todavía no aporta información útil.
- Ninguna variante logró las 4 posiciones en ninguna fecha.
- cruzada/v12 fue la mejor en reserva (37%), pero fue de las peores en aprendizaje; escogerla sería usar la reserva (regla 28.6).
- Estado: experimento documentado; no se incorpora al proceso.
