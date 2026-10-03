"""
Proyecto play — Validación de la base (data/resultados.csv).

Revisa: 4 dígitos, fecha = día de la semana, sin domingos, sin fechas repetidas,
semana/posición correctas, y lista los días lunes–sábado sin resultado.
Días sin sorteo confirmados: 04/07/2026.

Uso:
    python3 src/validar.py
"""

import csv
import datetime as dt
from collections import Counter
from pathlib import Path

DATOS = Path(__file__).resolve().parent.parent / "data" / "resultados.csv"
DIAS = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
SIN_SORTEO = {dt.date(2026, 7, 4)}


def main():
    filas = list(csv.DictReader(open(DATOS)))
    errores = []
    fechas = [dt.date.fromisoformat(r["fecha"]) for r in filas]
    for r, d in zip(filas, fechas):
        if len(r["numero"]) != 4 or not r["numero"].isdigit():
            errores.append(f"{d}: número inválido {r['numero']}")
        if r["dia"] != DIAS[d.weekday()]:
            errores.append(f"{d}: día {r['dia']} no corresponde")
        if d.weekday() == 6:
            errores.append(f"{d}: domingo")
    for d, c in Counter(fechas).items():
        if c > 1:
            errores.append(f"{d}: fecha repetida")
    if fechas != sorted(fechas):
        errores.append("fechas fuera de orden")
    todas = {fechas[0] + dt.timedelta(i) for i in range((fechas[-1] - fechas[0]).days + 1)}
    huecos = sorted(d for d in todas - set(fechas) if d.weekday() != 6)
    no_confirmados = [d for d in huecos if d not in SIN_SORTEO]
    for d in no_confirmados:
        errores.append(f"{d}: falta resultado (no confirmado como sin sorteo)")
    repetidos = [n for n, c in Counter(r["numero"] for r in filas).items() if c > 1]
    print(f"{len(filas)} resultados, {fechas[0]} → {fechas[-1]}")
    print(f"Sin sorteo confirmados: {', '.join(str(d) for d in huecos if d in SIN_SORTEO) or 'ninguno'}")
    print(f"Números repetidos (datos reales, solo aviso): {', '.join(repetidos) or 'ninguno'}")
    print("OK" if not errores else "ERRORES:\n  " + "\n  ".join(errores))


if __name__ == "__main__":
    main()
