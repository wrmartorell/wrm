# Proceso activo

Código: `src/proceso.py`. Actualizado: 03/10/2026.

1. **Base cronológica** (lunes a sábado; domingo = reset). 104 resultados, 01/06 → 30/09/2026. 04/07 sin sorteo. Validación: `src/validar.py`.
2. **Motor antiguo** (V1): toda la historia hasta el día anterior; repetidos una vez; S(y) = promedio de P(y|x); desempate dígito menor.
3. **Vertical**: (2·último − penúltimo) mod 10 por posición, mismo día de semana.
4. **Combinación 37.1** → Top 5 / Bottom 5.
5. **Regla del lunes** (aprobada 03/10): los lunes, los dígitos del resultado anterior (sábado) van primero en el orden del ranking; se completa con V1. Verificación: 16 lunes, ≥2 en Top 5 de 10/16 → 13/16.
6. **Grupos de permutación**: 715 → 55 → 10 cuando haya dígitos confirmados (criterio pendiente).

`src/v1.py` sigue congelado como referencia (24/24, 16/24, 6/24, 1/24).
