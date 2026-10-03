"""
Proyecto play — Paso 5: pares y tríos verdaderos dentro del ranking combinado.

No cambia ninguna fórmula. Para cada fecha (en orden, usando solo datos anteriores)
toma el ranking combinado #1..#10 y registra en qué posiciones quedaron los dígitos
reales. Luego cuenta, para cada par y trío de posiciones, cuántas veces todos sus
dígitos estaban en el número real (es decir, cuántas veces ese par/trío habría
reducido 715 → 55 / 55 → 10 sin perder el grupo real).

Uso:
    python3 src/pares_trios.py
"""

import datetime as dt
from itertools import combinations

from experimento_a import salida_ventana, nombre
from v1 import cargar

BLOQUE = (dt.date(2026, 8, 31), dt.date(2026, 9, 30))
VERSIONES = [None, 12, 18]


def medir(filas, ventana):
    fechas = [(d, n) for d, n in filas if BLOQUE[0] <= d <= BLOQUE[1]]
    pares = {p: 0 for p in combinations(range(1, 11), 2)}
    trios = {t: 0 for t in combinations(range(1, 11), 3)}
    patrones = []
    for fecha, real in fechas:
        comb = salida_ventana(filas, fecha, ventana)
        pos = sorted(comb.index(x) + 1 for x in set(real))
        patrones.append((fecha, real, "".join(comb), pos))
        for p in pares:
            pares[p] += set(p) <= set(pos)
        for t in trios:
            trios[t] += set(t) <= set(pos)
    return len(fechas), pares, trios, patrones


def main():
    filas = cargar()
    for v in VERSIONES:
        n, pares, trios, patrones = medir(filas, v)
        print(f"\n=== {nombre(v)} — {n} fechas ({BLOQUE[0]:%d/%m} → {BLOQUE[1]:%d/%m}) ===")
        print("Posiciones de los dígitos reales en el ranking combinado:")
        for fecha, real, comb, pos in patrones:
            print(f"  {fecha:%d/%m} {real}  ranking {comb}  reales en #{', #'.join(map(str, pos))}")
        top5p = {p: c for p, c in pares.items() if p[1] <= 5}
        print("\nPares dentro del Top 5 (veces que ambos fueron reales):")
        for p, c in sorted(top5p.items(), key=lambda x: (-x[1], x[0])):
            print(f"  #{p[0]}+#{p[1]}: {c}/{n} ({100*c/n:.0f}%)")
        print("Mejores pares en todo el ranking #1..#10:")
        for p, c in sorted(pares.items(), key=lambda x: (-x[1], x[0]))[:8]:
            print(f"  #{p[0]}+#{p[1]}: {c}/{n} ({100*c/n:.0f}%)")
        top5t = {t: c for t, c in trios.items() if t[2] <= 5}
        print("Tríos dentro del Top 5:")
        for t, c in sorted(top5t.items(), key=lambda x: (-x[1], x[0])):
            print(f"  #{t[0]}+#{t[1]}+#{t[2]}: {c}/{n} ({100*c/n:.0f}%)")
        print("Mejores tríos en todo el ranking #1..#10:")
        for t, c in sorted(trios.items(), key=lambda x: (-x[1], x[0]))[:6]:
            print(f"  #{t[0]}+#{t[1]}+#{t[2]}: {c}/{n} ({100*c/n:.0f}%)")


if __name__ == "__main__":
    main()
