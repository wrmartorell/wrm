# Paso 1 — Base cronológica: reevaluación

- 04/07/2026 (sábado): **sin sorteo**, confirmado. Esa semana tiene 5 resultados.
- La base ahora tiene `semana` y `pos_semana` (1.º–6.º de la semana). `src/validar.py` revisa la base.

## Firma del cruce de domingo (104 resultados)

| Transición | Comparten 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Dentro de la semana (86) | 19 | 33 | 23 | 10 | 1 |
| Cruzando el domingo (17) | 1 | 5 | **11** | 0 | 0 |

Se repite en junio-julio (5/8) y agosto-septiembre (6/9).

## Reset dentro del motor antiguo

| Bloque | V1 cadena | R1 sin cruces | R2 lunes aparte |
|---|---|---|---|
| Jun-jul (40): ≥2 / ≥3 / todos | 26 / 6 / 1 | 30 / 8 / 2 | 29 / 10 / 3 |
| Ago-sep (52): ≥2 / ≥3 / todos | 36 / 15 / 4 | 36 / 11 / 2 | 37 / 11 / 3 |

Mejora en jun-jul, igual en ≥2 y peor en ≥3 en ago-sep. No es estable: no se adopta por ahora.

## Lunes: dígitos del sábado primero

Para los lunes, los dígitos del sábado van primero (en el orden del ranking V1) y se completa con V1. 16 lunes (15/06 → 28/09).

| | ≥2 | ≥3 | Aciertos |
|---|---|---|---|
| V1 | 10/16 | 3 | 28 |
| Sábado primero | **13/16** | 3 | **31** |

Por período: jun-jul 4/7 → 6/7; ago-sep 6/9 → 7/9. Mejora en los dos. Muestra pequeña (16 lunes).
