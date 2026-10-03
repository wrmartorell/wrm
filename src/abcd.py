"""
Proyecto play — A/B/C/D integrado (pregunta 31.2): motor antiguo por posición.

No modifica V1. Misma idea del motor antiguo (transiciones históricas, promedio de
P, desempate dígito menor), pero el objetivo es el valor de cada posición del
número siguiente, no la simple presencia.

Variantes (definidas antes de correr):
- "misma": para la posición p, P(siguiente[p] = y | anterior[p] = x).
            Usa solo el valor que tenía esa misma posición.
- "cruzada": para la posición p, promedio sobre q en A/B/C/D de
            P(siguiente[p] = y | anterior[q] = x_q). Usa los 4 dígitos del último
            resultado, igual que el motor antiguo, pero apuntando a la posición p.
Historia: completa, ventana 12, ventana 18.

Combinación con vertical por posición (análoga a 37.1): Top 2 posicional;
el valor vertical de esa posición; primero el que coincide, luego el resto del
Top 2, luego el vertical, luego el resto del ranking posicional.

Bloques: aprendizaje 15/08 → 29/08 (13); reserva 31/08 → 30/09 (27; 28–30/09 eran
conocidos). Criterio de la ganadora (solo aprendizaje): más fechas con ≥3
posiciones reales dentro del Top 3 de su posición → más aciertos posicionales en
Top 3 → más aciertos en #1.

Uso:
    python3 src/abcd.py
"""

import datetime as dt

from v1 import cargar, motor_vertical

DIGITOS = "0123456789"
APRENDIZAJE = (dt.date(2026, 8, 15), dt.date(2026, 8, 29))
RESERVA = (dt.date(2026, 8, 31), dt.date(2026, 9, 30))
VARIANTES = [(m, v) for m in ("misma", "cruzada") for v in (None, 12, 18)]
POS = "ABCD"


def nombre(var):
    m, v = var
    return f"{m}/{'completa' if v is None else 'v' + str(v)}"


def ranking_posicional(historia, p, modo):
    ult = historia[-1]
    trans = list(zip(historia, historia[1:]))
    fuentes = [p] if modo == "misma" else range(4)
    S = {}
    for y in DIGITOS:
        tot = 0.0
        for q in fuentes:
            con = [(a, b) for a, b in trans if a[q] == ult[q]]
            if con:
                tot += sum(1 for _, b in con if b[p] == y) / len(con)
        S[y] = tot / len(fuentes)
    return sorted(DIGITOS, key=lambda y: (-round(S[y], 12), int(y)))


def combinar(rank, vert_valor):
    orden = ([vert_valor] if vert_valor in rank[:2] else []) + rank[:2] + [vert_valor] + rank
    out = []
    for d in orden:
        if d not in out:
            out.append(d)
    return out


def salida(filas, fecha, var):
    modo, ventana = var
    historia = [n for d, n in filas if d < fecha]
    if ventana is not None:
        historia = historia[-ventana:]
    vert = motor_vertical(filas, fecha)
    return [combinar(ranking_posicional(historia, p, modo), vert[p]) for p in range(4)], vert


def evaluar(filas, var, bloque):
    m = {"n": 0, "top1": 0, "top3": 0, "ge3": 0, "c4": 0, "pos_top3": [0] * 4, "det": []}
    for fecha, real in [(d, n) for d, n in filas if bloque[0] <= d <= bloque[1]]:
        ranks, vert = salida(filas, fecha, var)
        en3 = [real[p] in ranks[p][:3] for p in range(4)]
        m["n"] += 1
        m["top1"] += sum(real[p] == ranks[p][0] for p in range(4))
        m["top3"] += sum(en3)
        m["ge3"] += sum(en3) >= 3
        m["c4"] += all(en3)
        for p in range(4):
            m["pos_top3"][p] += en3[p]
        m["det"].append((fecha, real, ["".join(r[:3]) for r in ranks], sum(en3)))
    return m


def tabla(titulo, res):
    print(f"\n{titulo}")
    print(f"{'variante':<18}{'≥3 pos':>9}{'4 pos':>8}{'top3':>8}{'#1':>6}   A  B  C  D (top3)")
    for var, m in res.items():
        n = m["n"]
        print(f"{nombre(var):<18}{m['ge3']:>5}/{n:<3}{m['c4']:>4}/{n:<3}{m['top3']:>4}/{4*n:<3}{m['top1']:>4}   "
              + "  ".join(str(x) for x in m["pos_top3"]))


def main():
    filas = cargar()
    apr = {var: evaluar(filas, var, APRENDIZAJE) for var in VARIANTES}
    tabla("APRENDIZAJE 15/08 → 29/08", apr)
    gan = sorted(VARIANTES, key=lambda v: (-apr[v]["ge3"], -apr[v]["top3"], -apr[v]["top1"]))[0]
    print(f"\nGanadora congelada antes de la reserva: {nombre(gan)}")

    res = {var: evaluar(filas, var, RESERVA) for var in VARIANTES}
    tabla("RESERVA 31/08 → 30/09", res)
    print(f"\nDetalle reserva — ganadora {nombre(gan)} (Top 3 por posición A | B | C | D)")
    for fecha, real, t3, k in res[gan]["det"]:
        print(f"  {fecha:%d/%m} {real}  {' | '.join(t3)}  → {k}/4 posiciones")

    # Vertical sola por posición, como referencia.
    v1 = v4 = 0
    for fecha, real in [(d, n) for d, n in filas if RESERVA[0] <= d <= RESERVA[1]]:
        vert = motor_vertical(filas, fecha)
        v1 += sum(real[p] == vert[p] for p in range(4))
    print(f"\nReferencia: vertical sola acierta valor exacto en {v1}/{4*res[gan]['n']} posiciones (reserva)")

    fecha = dt.date(2026, 10, 1)
    ranks, vert = salida(filas, fecha, gan)
    print(f"\n01/10/2026 — {nombre(gan)} (vertical {vert})")
    for p in range(4):
        print(f"  {POS[p]}: {' '.join(ranks[p])}")
    return gan


if __name__ == "__main__":
    main()
