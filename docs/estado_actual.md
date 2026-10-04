# Estado actual del proyecto — punto de regreso

Actualizado: 04/10/2026. Al retomar, empezar aquí.

## Proceso activo (`src/proceso.py`, detalle en `proceso_activo.md`)

1. Base cronológica: 01/06 → 02/10/2026 (106 resultados). 04/07 sin sorteo. Validación: `src/validar.py`.
2. Motor antiguo (V1, sin cambios).
3. Señal de los 2 días anteriores (reemplaza la vertical).
4. Plan de protección: Top 4 del motor antiguo fijo; la señal solo decide #5 y el Bottom.
5. Regla del lunes: los dígitos del sábado van primero.
6. Bottom 5: revisado, sin cambios.
7. Grupos de permutación: Top 7 → 161 grupos (sin tríos ni cuatro iguales) → ordenados por dígitos compartidos con ayer + tipo de grupo → primeros 35.

Regla para aceptar cambios: no empeorar en ningún período (jun-jul, ago-sep) y mejorar en al menos uno.

## Rendimiento (meta: los 4 dígitos)

| Medida | Jun-jul (40) | Ago-sep (52) |
|---|---|---|
| ≥2 en Top 5 | 73% | 73% |
| Los 4 dígitos en Top 7 | 25% | 35% |
| Grupo real en los primeros 35 | 15% | 21% |

## Pruebas ciegas (congeladas antes del resultado, en `predicciones/`)

| Fecha | Real | Proceso activo (Top 5 / Top 7) | ¿Los 4 en Top 7? | V2 (observación) |
|---|---|---|---|---|
| 01/10 | 9281 | 2 / 2 | no | 4 en Top 7, grupo en lugar 2 |
| 02/10 | 0505 | 1 / 1 (de 2 dígitos) | no | 2 de 2 en Top 5 |
| 03/10 | (no revelado) | 2 / 3 | no | pendiente |

01/10: la salida del proceso activo se calculó después de conocer aciertos parciales (no totalmente ciega).

## Dos selecciones (A + B) — documentado, NO se usa por ahora (decisión del usuario 04/10)

- A = proceso activo (Top 7 → grupos); B = V2 (Top 7 → grupos). 35 grupos en total, alternando A y B.
- Grupo real en los 35: jun-jul 15% → **22%**, ago-sep 21% → **21%**; ciegas 1/2 (vs 0/2). Pasa la regla.
- Las dos completas (~63 grupos): 32–33%.
- Dos selecciones de exactamente 4 dígitos: 2–8% (descartado).
- 03/10 ya tiene la lista A + B en `predicciones/2026-10-03.md`.

## Próximos pasos (acordados, en orden)

1. Pruebas ciegas todos los días: congelar antes de cada resultado; meta 20–30 días.
2. Conseguir más historia (antes de junio).
3. V2 en paralelo. Regla fijada: si después de 20 días ciegos V2 tiene más días con los 4 dígitos en el Top 7, se cambia.
4. Probar el orden dentro del grupo (el dígito casi nunca repite posición al día siguiente) para bajar los 24 órdenes por grupo.

Nota: ningún método ha mostrado todavía una mejora sostenida en todos los períodos y en las pruebas ciegas.
