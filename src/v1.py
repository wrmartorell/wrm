"""
Proyecto play — Versión 1 (CONGELADA).

No modificar este archivo. Todo experimento nuevo va en otro archivo y se
compara contra esta versión.

Definición: ver docs/version1.md.

Uso:
    python3 src/v1.py             # backtest de verificación 31/08 → 26/09
    python3 src/v1.py --siguiente # salida para la fecha siguiente al último dato autoritativo
"""

import csv
import datetime as dt
import sys
from pathlib import Path

DATOS = Path(__file__).resolve().parent.parent / "data" / "resultados.csv"
DIGITOS = "0123456789"

# Top 4 del motor antiguo registrados en la sección 23 (referencia de verificación).
TOP4_REGISTRADO = {
    "2026-08-31": "4583", "2026-09-01": "4852", "2026-09-02": "4586", "2026-09-03": "4586",
    "2026-09-04": "4586", "2026-09-05": "4581", "2026-09-07": "4532", "2026-09-08": "4582",
    "2026-09-09": "4358", "2026-09-10": "4835", "2026-09-11": "5483", "2026-09-12": "4582",
    "2026-09-14": "4538", "2026-09-15": "4587", "2026-09-16": "4735", "2026-09-17": "4685",
    "2026-09-18": "4758", "2026-09-19": "4538", "2026-09-21": "4856", "2026-09-22": "4378",
    "2026-09-23": "4573", "2026-09-24": "7453", "2026-09-25": "3487", "2026-09-26": "8453",
}


def cargar(estados=("autoritativo",)):
    """Devuelve [(fecha, numero)] en orden cronológico, solo con los estados pedidos."""
    with open(DATOS, newline="") as f:
        filas = [r for r in csv.DictReader(f) if r["estado"] in estados]
    return [(dt.date.fromisoformat(r["fecha"]), r["numero"]) for r in filas]


def motor_antiguo(historia):
    """
    Transiciones por presencia de dígitos.
    - historia: lista de números hasta el resultado inmediatamente anterior (cadena, sin reset).
    - Repetidos cuentan una vez.
    - S(y) = promedio sobre x en U del último resultado de P(y|x).
    - Desempate: dígito menor primero.
    """
    U = set(historia[-1])
    transiciones = list(zip(historia, historia[1:]))
    S = {}
    for y in DIGITOS:
        total = 0.0
        for x in U:
            con_x = [(a, b) for a, b in transiciones if x in a]
            if con_x:
                total += sum(1 for _, b in con_x if y in b) / len(con_x)
        S[y] = total / len(U)
    ranking = sorted(DIGITOS, key=lambda y: (-round(S[y], 12), int(y)))
    return ranking, S


def motor_vertical(filas, fecha):
    """
    Mismo día de semana: X(n+1) = (2·X(n) − X(n−1)) mod 10, por posición A/B/C/D,
    usando los dos resultados anteriores de ese día de semana.
    """
    previos = [n for d, n in filas if d < fecha and d.weekday() == fecha.weekday()]
    if len(previos) < 2:
        return None
    a, b = previos[-2], previos[-1]
    return "".join(str((2 * int(b[p]) - int(a[p])) % 10) for p in range(4))


def combinado(ranking, vertical):
    """Suma de evidencia, sección 37.1."""
    top4 = ranking[:4]
    vd = list(dict.fromkeys(vertical or ""))  # dígitos distintos, orden A→D
    orden = [x for x in top4 if x in vd] + top4 + vd + ranking
    salida = []
    for d in orden:
        if d not in salida:
            salida.append(d)
    return salida


def salida(filas, fecha):
    """Salida congelable para una fecha usando solo datos anteriores a ella."""
    historia = [n for d, n in filas if d < fecha]
    ranking, S = motor_antiguo(historia)
    vert = motor_vertical(filas, fecha)
    comb = combinado(ranking, vert)
    return {"ranking_antiguo": ranking, "S": S, "vertical": vert, "combinado": comb}


def backtest(desde=dt.date(2026, 8, 31), hasta=dt.date(2026, 9, 26)):
    filas = cargar()
    objetivos = [(d, n) for d, n in filas if desde <= d <= hasta]
    coinciden = c2 = c3 = c4 = aciertos = 0
    faltantes = {k: 0 for k in range(6, 11)}
    print("fecha       real  top4  reg.  vert  top5   aciertos  rango_reales")
    for fecha, real in objetivos:
        s = salida(filas, fecha)
        top4 = "".join(s["ranking_antiguo"][:4])
        top5 = s["combinado"][:5]
        h = len(set(real) & set(top5))
        reg = TOP4_REGISTRADO.get(fecha.isoformat(), "----")
        coinciden += top4 == reg
        aciertos += h
        c2 += h >= 2
        c3 += h >= 3
        c4 += h >= 4
        rangos = {x: s["combinado"].index(x) + 1 for x in sorted(set(real))}
        for x, r in rangos.items():
            if r > 5:
                faltantes[r] += 1
        marca = "" if top4 == reg else "  <-- DIFIERE"
        print(f"{fecha}  {real}  {top4}  {reg}  {s['vertical']}  {''.join(top5)}  {h}         "
              f"{' '.join(f'{x}:#{r}' for x, r in rangos.items())}{marca}")
    n = len(objetivos)
    print(f"\nTop 4 antiguo igual al registrado: {coinciden}/{n}")
    print(f"Top 5 combinado: >=2 -> {c2}/{n} | >=3 -> {c3}/{n} | 4 -> {c4}/{n} | aciertos -> {aciertos}")
    print("Dígitos reales fuera del Top 5 por posición: "
          + ", ".join(f"#{k}={v}" for k, v in faltantes.items()))


def siguiente():
    filas = cargar()
    ultimo = filas[-1][0]
    fecha = ultimo + dt.timedelta(days=1)
    if fecha.weekday() == 6:  # domingo: no hay número
        fecha += dt.timedelta(days=1)
    s = salida(filas, fecha)
    print(f"Fecha objetivo: {fecha} (datos hasta {ultimo})")
    print("Ranking antiguo:", " ".join(f"{y}({s['S'][y]:.3f})" for y in s["ranking_antiguo"]))
    print("Vertical:", s["vertical"])
    print("Combinado:", " ".join(s["combinado"]), "| Top 5:", " ".join(s["combinado"][:5]))


if __name__ == "__main__":
    siguiente() if "--siguiente" in sys.argv else backtest()
