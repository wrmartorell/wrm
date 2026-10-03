# Experimento A — Ventanas históricas del motor antiguo

Fecha: 3 de octubre de 2026. Código: `src/experimento_a.py`. La Versión 1 no se modificó.

## Definiciones aprobadas antes de correr

- Ventana N = últimos N resultados antes de la fecha objetivo (N−1 transiciones). Si hay menos de N, se usa toda la historia disponible.
- Ventanas: 6, 12, 18 e historia completa (= V1).
- Vertical y combinado: exactamente como V1.
- Aprendizaje: 15/08 → 29/08 (13 fechas; la vertical necesita dos días iguales previos).
- Reserva: 31/08 → 26/09 (24 fechas).
- Criterio de ganadora (solo aprendizaje): más fechas con ≥2 en Top 5 combinado → más aciertos → historia completa.

## Aprendizaje (13 fechas)

| Motor antiguo | ≥2 | ≥3 | 4 | Aciertos |
|---|---|---|---|---|
| Ventana 6 | 10/13 | 3/13 | 0/13 | 26 |
| **Ventana 12** | **10/13** | **5/13** | 0/13 | **28** |
| Ventana 18 | 8/13 | 4/13 | 0/13 | 25 |
| Completa (V1) | 9/13 | 2/13 | 0/13 | 24 |

**Ganadora congelada antes de la reserva: ventana 12** (empate en ≥2 con ventana 6; gana por aciertos 28 vs 26).

## Reserva (24 fechas)

| Motor antiguo | ≥2 | ≥3 | 4 | Aciertos | Fuera Top 5 #6/#7/#8/#9/#10 |
|---|---|---|---|---|---|
| Ventana 6 | 15/24 | 4/24 | 0/24 | 41 | 11/5/10/8/10 |
| **Ventana 12 (ganadora)** | **17/24** | **6/24** | **1/24** | **46** | 6/8/6/8/11 |
| Ventana 18 | 17/24 | 6/24 | 2/24 | 49 | 4/10/5/6/11 |
| Completa (V1) | 16/24 | 6/24 | 1/24 | 47 | 7/9/7/8/7 |

## Lectura

- La ventana 12, escogida solo con agosto, en la reserva logró 17/24 con ≥2 (V1: 16/24), igual en ≥3 (6/24) y en 4 (1/24), y 46 aciertos (V1: 47).
- La ventana 18 fue la mejor en la reserva (17/24, 6/24, 2/24, 49), pero fue la peor en aprendizaje; escogerla ahora sería usar la reserva para elegir (regla 28.6).
- La ventana 6 fue la más débil en la reserva.
- Los casos de 4 dígitos en reserva: ventana 12 → 26/09 (8173); ventana 18 → 09/09 (4378) y 26/09 (8173).
- Las diferencias entre ventanas son de 1–2 fechas sobre 24.

## Estado

Resultado documentado. **No cambia la Versión 1** hasta que el usuario decida.
