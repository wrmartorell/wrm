# Versión 1 — CONGELADA

Fecha de congelación: 3 de octubre de 2026.
Implementación: `src/v1.py`. Datos: `data/resultados.csv`.

Esta versión no se modifica. Todo experimento futuro se compara contra ella sin cambiarla retroactivamente.

## Motor antiguo

- **Historia:** toda la historia disponible hasta el resultado inmediatamente anterior (ventana expansiva). Para predecir el 31 de agosto se usa 1 → 29 de agosto; para el 1 de septiembre, 1 → 31 de agosto, etc.
- **Cadena:** todos los registros consecutivos forman una sola cadena; este motor **no** aplica reset sábado→lunes.
- **Repetidos:** cuentan una vez (8518 → {8,5,1}), tanto en el resultado de origen como en el siguiente.
- **Señal:** si el último resultado tiene los dígitos distintos U = {x₁,…,xₘ}, para cada candidato y ∈ {0,…,9}:

  P(y|x) = #{transiciones donde x estaba presente y y apareció en el siguiente} / #{transiciones donde x estaba presente}

  S(y) = (1/|U|) · Σ_{x∈U} P(y|x)  — promedio con el mismo peso.
- **Ranking:** los 10 dígitos de mayor a menor S(y).
- **Desempate:** si las puntuaciones son iguales, dígito menor primero (0 → 9).

## Motor vertical

- Para un día dado se toman los dos resultados anteriores del mismo día de semana.
- Por posición A, B, C y D, de forma independiente:

  X(n+1) = (2·X(n) − X(n−1)) mod 10

- Ejemplo, miércoles 9 de septiembre: 26/08 = 9426, 02/09 = 3654 → **7882**.

## Combinado (suma de evidencia, sección 37.1)

1. Ranking completo del motor antiguo.
2. Top 4 inicial del antiguo.
3. Proyección vertical del mismo día.
4. Dígitos distintos de la vertical, en orden A → B → C → D.
5. Primero los dígitos que están en el Top 4 antiguo y en la vertical (en el orden del antiguo).
6. Luego el resto del Top 4 antiguo, en su orden.
7. Luego los dígitos verticales que faltan.
8. Se completa con el ranking completo del antiguo.
9. Top 5 combinado = primeros cinco.

## Verificación (backtest 31/08 → 26/09, 24 fechas)

| Verificación | Registrado | `src/v1.py` |
|---|---|---|
| Top 4 antiguo (sección 23) | 24 rankings | 24/24 idénticos |
| Top 5 con mínimo 2 dígitos | 16/24 | 16/24 |
| Top 5 con mínimo 3 dígitos | 6/24 | 6/24 |
| Top 5 con los 4 dígitos | 1/24 | 1/24 |
| Aciertos acumulados Top 5 | 47 | 47 |
| Faltantes #6/#7/#8/#9/#10 | 7/9/7/8/7 | 7/9/7/8/7 |

## Datos

- Base autoritativa: 1 de agosto → 26 de septiembre de 2026.
- 28, 29 y 30 de septiembre: ya conocidos (sección 9.4); solo auditoría.
- 1 de octubre: contaminado metodológicamente; excluido.
- La reserva limpia comienza en la primera fecha cuyo resultado no se haya discutido de ninguna forma.
- 3654 aparece dos veces (miércoles 19/08 y miércoles 02/09): dato real.

## Leyenda de seguimiento (no son filtros)

- Sábado → lunes: en 6 de 9 cambios de semana el lunes compartió exactamente 2 dígitos con el sábado.
- Miércoles: grupos repetidos 3456 (3654, 3654) y 3478 (4738, 4378).
- Posición D: el 9 no ha salido en D en los 52 resultados.

## Próximos pasos aprobados (orden)

1. ✅ Fórmulas exactas.
2. ✅ Congelar versión 1.
3. Experimento A: ventanas 6, 12, 18 e historia completa (agosto = aprendizaje, septiembre = reserva).
4. Medir pares y tríos verdaderos dentro del ranking (conexión con 715 → 55 → 10).
5. Reserva nueva limpia.
6. Seguimiento de la leyenda.
