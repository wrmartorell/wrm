"""
Proyecto play — Versión 2: motor antiguo sin frecuencia + reset del domingo.

V1 queda intacta (src/v1.py). Cambios aprobados:

1. Efecto en vez de conteo:
       efecto(y | x) = P(y aparece en el siguiente | x estaba presente) − P(y aparece en el siguiente)
   S(y) = promedio de efecto(y | x) sobre los dígitos distintos x del último resultado.
   Un dígito que sale siempre no gana nada; sube solo lo que x hace cambiar.
2. Reset del domingo dentro del motor:
   - Para predecir martes→sábado: solo transiciones dentro de la semana (lun→mar … vie→sáb).
   - Para predecir lunes: solo transiciones sábado→lunes (el lunes se lee aparte).

Igual que V1: repetidos cuentan una vez, desempate dígito menor, historia completa,
vertical y combinado de la sección 37.1.

Uso:
    python3 src/v2.py              # aprendizaje + reserva, comparado con V1
    python3 src/v2.py 2026-10-01   # salida para una fecha
"""

import datetime as dt
import sys

from v1 import DIGITOS, cargar, combinado, motor_vertical
from v1 import salida as salida_v1

APRENDIZAJE = (dt.date(2026, 8, 15), dt.date(2026, 8, 29))
RESERVA = (dt.date(2026, 8, 31), dt.date(2026, 9, 30))


def transiciones(previos, lunes):
    """Pares consecutivos respetando el reset del domingo."""
    pares = []
    for (d1, a), (d2, b) in zip(previos, previos[1:]):
        cruza_domingo = d2.weekday() == 0 and d1 < d2  # cualquier paso a lunes cruza el domingo (ej. vie→lun si falta el sábado)
        if lunes == cruza_domingo:
            pares.append((a, b))
    return pares


def motor_efecto(filas, fecha):
    previos = [(d, n) for d, n in filas if d < fecha]
    pares = transiciones(previos, lunes=fecha.weekday() == 0)
    U = set(previos[-1][1])
    S = {}
    for y in DIGITOS:
        base = sum(1 for _, b in pares if y in b) / len(pares) if pares else 0.0
        tot = 0.0
        for x in U:
            con_x = [(a, b) for a, b in pares if x in a]
            if con_x:
                tot += sum(1 for _, b in con_x if y in b) / len(con_x) - base
        S[y] = tot / len(U)
    ranking = sorted(DIGITOS, key=lambda y: (-round(S[y], 12), int(y)))
    return ranking, S


def salida(filas, fecha):
    ranking, S = motor_efecto(filas, fecha)
    vert = motor_vertical(filas, fecha)
    return {"ranking_antiguo": ranking, "S": S, "vertical": vert, "combinado": combinado(ranking, vert)}


def evaluar(filas, fn, bloque):
    m = {"n": 0, "ge2": 0, "ge3": 0, "todos": 0, "aciertos": 0, "pos": [0] * 10, "top4": {}}
    for fecha, real in [(d, n) for d, n in filas if bloque[0] <= d <= bloque[1]]:
        s = fn(filas, fecha)
        comb = s["combinado"]
        h = len(set(real) & set(comb[:5]))
        m["n"] += 1
        m["aciertos"] += h
        m["ge2"] += h >= 2
        m["ge3"] += h >= 3
        m["todos"] += set(real) <= set(comb[:5])
        for x in set(real):
            m["pos"][comb.index(x)] += 1
        for d in s["ranking_antiguo"][:4]:
            m["top4"][d] = m["top4"].get(d, 0) + 1
    return m


def reporte():
    filas = cargar()
    for titulo, bloque in (("APRENDIZAJE 15/08 → 29/08", APRENDIZAJE), ("RESERVA 31/08 → 30/09", RESERVA)):
        print(f"\n{titulo}")
        for nombre, fn in (("V1", salida_v1), ("V2", salida)):
            m = evaluar(filas, fn, bloque)
            n = m["n"]
            print(f"  {nombre}: ≥2 {m['ge2']}/{n} | ≥3 {m['ge3']}/{n} | todos {m['todos']}/{n} | aciertos {m['aciertos']}")
            print(f"      reales por posición #1..#10: {' '.join(map(str, m['pos']))}")
            fijos = sorted(m["top4"].items(), key=lambda x: -x[1])[:5]
            print(f"      dígitos más repetidos en Top 4 antiguo: {', '.join(f'{d}({c}/{n})' for d, c in fijos)}")


def una_fecha(fecha):
    filas = cargar()
    s = salida(filas, fecha)
    print(f"V2 — {fecha} ({'lunes: transiciones sábado→lunes' if fecha.weekday() == 0 else 'transiciones dentro de la semana'})")
    print("Efecto: " + "  ".join(f"{y}({s['S'][y]:+.3f})" for y in s["ranking_antiguo"]))
    print(f"Vertical: {s['vertical']}")
    print(f"Combinado: {' '.join(s['combinado'])} | Top 5: {' '.join(s['combinado'][:5])}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        una_fecha(dt.date.fromisoformat(sys.argv[1]))
    else:
        reporte()
