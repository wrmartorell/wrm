# Paso 5 — Pares y tríos en el ranking combinado

Código: `src/pares_trios.py`. Ninguna fórmula cambia. 27 fechas (31/08 → 30/09), en orden, cada una con solo datos anteriores.
Pregunta: si se toma el par (o trío) en posiciones fijas del ranking, ¿cuántas veces ambos (o los tres) dígitos eran reales? Eso es lo que permite 715 → 55 (par) o 55 → 10 (trío) sin perder el grupo real.

## Mejor par y trío por versión

| Versión | Mejor par del Top 5 | Mejor trío del Top 5 | #1 es real |
|---|---|---|---|
| V1 (completa) | #2+#5: 6/27 (22%) | #1+#2+#3 / #1+#3+#5 / #2+#3+#5: 2/27 (7%) | 12/27 (44%) |
| Ventana 12 | #1+#4: 7/27 (26%) | #1+#2+#5: 3/27 (11%) | 14/27 (52%) |
| Ventana 18 | #1+#2: 6/27 (22%) | varios: 2/27 (7%) | 14/27 (52%) |

## Lectura

- Ningún par en posición fija acierta más de 26% de las veces; ningún trío más de 11%.
- El "mejor" par cambia según la versión (#2+#5, #1+#4, #1+#2): no hay una posición estable.
- La posición #1 es la más confiable: es real cerca de la mitad de las veces.
- Conclusión: escoger el par/trío por posición fija no sirve para reducir 715 → 55 → 10 sin perder el grupo real. Hace falta otra señal que diga cuál par.
