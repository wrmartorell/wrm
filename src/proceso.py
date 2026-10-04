"""
Proyecto play — Proceso activo.

1. Base cronológica (lunes a sábado; domingo = reset; 04/07/2026 sin sorteo).
2. Motor antiguo (V1, sin cambios): toda la historia, S(y) promedio de P(y|x).
3. Señal de los 2 días anteriores (aprobada 04/10/2026, reemplaza a la vertical):
   por cada posición A/B/C/D,
   - día anterior: su valor + el salto más común de un día a otro en esa posición;
   - dos días antes: su valor + el salto más común a dos días en esa posición.
   Los saltos se calculan solo con la historia anterior a la fecha.
4. Plan de protección (aprobado 04/10/2026): el Top 4 del motor antiguo queda fijo;
   la señal de los 2 días solo decide el #5 y el orden del #6 al #10.
5. Regla del lunes (aprobada 03/10/2026): los lunes, los dígitos del resultado anterior
   (sábado) van primero, en el orden del ranking.

Uso:
    python3 src/proceso.py              # verificación jun-jul / ago-sep
    python3 src/proceso.py 2026-10-05   # salida para una fecha
"""

import datetime as dt
import sys
from collections import Counter

from v1 import cargar, motor_antiguo

TODO = ("historico_previo", "autoritativo")
BLOQUES = [("Jun-jul", dt.date(2026, 6, 15), dt.date(2026, 7, 31)),
           ("Ago-sep", dt.date(2026, 8, 1), dt.date(2026, 9, 30))]


def senal_dos_dias(previos):
    """Proyección por posición desde el día anterior y desde dos días antes."""
    def proyeccion(lag):
        base = previos[-lag]
        pares = list(zip(previos, previos[lag:]))
        out = ""
        for p in range(4):
            saltos = Counter((int(b[p]) - int(a[p])) % 10 for a, b in pares)
            s = sorted(range(10), key=lambda k: (-saltos[k], k))[0]
            out += str((int(base[p]) + s) % 10)
        return out
    return proyeccion(1), proyeccion(2)


def salida(filas, fecha):
    previos = [n for d, n in filas if d < fecha]
    ranking, S = motor_antiguo(previos)
    p1, p2 = senal_dos_dias(previos)
    senal = set(p1 + p2)
    top4 = ranking[:4]
    resto = [x for x in ranking[4:] if x in senal] + [x for x in ranking[4:] if x not in senal]
    comb = top4 + resto
    if fecha.weekday() == 0:
        primero = [x for x in comb if x in set(previos[-1])]
        comb = primero + [x for x in comb if x not in primero]
    return {"ranking_antiguo": ranking, "S": S, "dia_anterior": p1, "dos_dias": p2, "combinado": comb}


def verificar():
    filas = cargar(estados=TODO)
    for nombre, a, b in BLOQUES:
        n = ge2 = ge3 = aciertos = 0
        for d, real in [(d, x) for d, x in filas if a <= d <= b]:
            h = len(set(real) & set(salida(filas, d)["combinado"][:5]))
            n += 1
            ge2 += h >= 2
            ge3 += h >= 3
            aciertos += h
        print(f"{nombre}: ≥2 {ge2}/{n} | ≥3 {ge3}/{n} | aciertos {aciertos}")


def una_fecha(fecha):
    filas = cargar(estados=TODO)
    s = salida(filas, fecha)
    print(f"{fecha}: ranking antiguo {' '.join(s['ranking_antiguo'])}")
    print(f"Señal 2 días: día anterior → {s['dia_anterior']} | dos días antes → {s['dos_dias']}")
    print(f"Top 5 {' '.join(s['combinado'][:5])} | Bottom 5 {' '.join(s['combinado'][5:])}")


if __name__ == "__main__":
    una_fecha(dt.date.fromisoformat(sys.argv[1])) if len(sys.argv) > 1 else verificar()
