"""
Proyecto play — Congelar la salida de una fecha antes de conocer su resultado.

Usa solo resultados anteriores a la fecha objetivo. Produce la salida de:
- V1 (motor antiguo con historia completa) — versión oficial.
- Ventana 12 (ganadora del Experimento A) — en observación.

Uso:
    python3 src/congelar.py 2026-10-01
"""

import datetime as dt
import sys
from pathlib import Path

from experimento_a import salida_ventana
from v1 import cargar, motor_antiguo, motor_vertical

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
VERSIONES = [("V1 — historia completa (oficial)", None), ("Ventana 12 (en observación)", 12)]


def bloque(filas, fecha, ventana):
    historia = [n for d, n in filas if d < fecha]
    if ventana is not None:
        historia = historia[-ventana:]
    ranking, S = motor_antiguo(historia)
    comb = salida_ventana(filas, fecha, ventana)
    return ranking, S, comb


def main(fecha):
    filas = cargar()
    previos = [(d, n) for d, n in filas if d < fecha]
    if any(d >= fecha for d, _ in filas):
        sys.exit(f"La base ya contiene {fecha} o fechas posteriores: no se puede congelar a ciegas.")
    if fecha.weekday() == 6:
        sys.exit("Domingo no tiene número.")

    vert = motor_vertical(filas, fecha)
    mismos = [(d, n) for d, n in previos if d.weekday() == fecha.weekday()][-2:]
    L = [f"# Salida congelada — {DIAS[fecha.weekday()]} {fecha.strftime('%d/%m/%Y')}", "",
         f"Datos usados: {previos[0][0].strftime('%d/%m')} → {previos[-1][0].strftime('%d/%m/%Y')} "
         f"({len(previos)} resultados). Último: {previos[-1][1]}.", "",
         "Congelada antes de conocer el resultado. No se modifica después.", "",
         "## Vertical", "",
         f"Mismo día anterior: {mismos[0][0].strftime('%d/%m')} = {mismos[0][1]}, "
         f"{mismos[1][0].strftime('%d/%m')} = {mismos[1][1]} → **{vert}** (A={vert[0]} B={vert[1]} C={vert[2]} D={vert[3]})", ""]
    for titulo, v in VERSIONES:
        ranking, S, comb = bloque(filas, fecha, v)
        L += [f"## {titulo}", "",
              "Ranking antiguo: " + "  ".join(f"{y} ({S[y]:.3f})" for y in ranking), "",
              f"Top 4 antiguo: **{' '.join(ranking[:4])}**", "",
              f"Combinado completo: {' '.join(comb)}", "",
              f"**Top 5 combinado: {' '.join(comb[:5])}**  |  Bottom 5: {' '.join(comb[5:])}", ""]
    L += ["## Resultado real", "", "_Pendiente._", ""]

    out = Path(__file__).resolve().parent.parent / "docs" / "predicciones" / f"{fecha.isoformat()}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(L))
    print("\n".join(L))
    print(f"\nGuardado en {out}")


if __name__ == "__main__":
    main(dt.date.fromisoformat(sys.argv[1]))
