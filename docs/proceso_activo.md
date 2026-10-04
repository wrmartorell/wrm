# Proceso activo

Código: `src/proceso.py`. Actualizado: 04/10/2026.

1. **Base cronológica** (lunes a sábado; domingo = reset). 104 resultados, 01/06 → 30/09/2026. 04/07 sin sorteo. Validación: `src/validar.py`.
2. **Motor antiguo** (V1, sin cambios): toda la historia; repetidos una vez; S(y) = promedio de P(y|x); desempate dígito menor.
3. **Señal de los 2 días anteriores** (aprobada 04/10, reemplaza a la vertical): por posición A/B/C/D, el día anterior + su salto más común de un día, y dos días antes + su salto más común a dos días (solo historia previa).
4. **Plan de protección** (aprobado 04/10): el Top 4 del motor antiguo queda fijo; la señal de los 2 días solo decide el #5 y el orden del #6–#10. Un cambio nuevo se acepta solo si no empeora en ningún período y mejora en al menos uno.
5. **Regla del lunes** (aprobada 03/10): los lunes, los dígitos del sábado van primero.
6. **Grupos de permutación** (aprobado 04/10): grupos del Top 7 sin tríos ni cuatro iguales (161), ordenados por dígitos compartidos con ayer + tipo de grupo; se usan los primeros 35. Verificación: grupo real en los primeros 35 en 6/40 (jun-jul) y 11/52 (ago-sep).

## Verificación (fecha por fecha)

| Bloque | ≥2 | ≥3 | Aciertos |
|---|---|---|---|
| Jun-jul (40) | 29 | 12 | 81 |
| Ago-sep (52) | 38 | 16 | 103 |

Antes (V1 + vertical + lunes): jun-jul 28 / 5 / 73; ago-sep 37 / 16 / 101.

`src/v1.py` sigue congelado como referencia (24/24, 16/24, 6/24, 1/24).
