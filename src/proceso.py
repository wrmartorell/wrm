"""
Proyecto play — Proceso activo.

= V1 (src/v1.py, sin modificar: motor antiguo + vertical + combinación 37.1),
  con toda la historia disponible,
+ regla del lunes (aprobada 03/10/2026): para un lunes, los dígitos distintos del
  resultado anterior (el sábado; si no hubo sorteo, el último día de esa semana)
  van primero, en el orden del ranking combinado V1; después se completa con V1.
  Martes a sábado: V1 sin cambios.

Uso:
    python3 src/proceso.py              # verificación en los lunes 15/06 → 28/09
    python3 src/proceso.py 2026-10-05   # salida para una fecha
"""

import datetime as dt
import sys

from v1 import cargar
from v1 import salida as salida_v1

TODO = ("historico_previo", "autoritativo")


def salida(filas, fecha):
    s = salida_v1(filas, fecha)
    comb = s["combinado"]
    if fecha.weekday() == 0:
        anterior = [n for d, n in filas if d < fecha][-1]
        primero = [x for x in comb if x in set(anterior)]
        comb = primero + [x for x in comb if x not in primero]
        s["regla_lunes"] = anterior
    s["combinado"] = comb
    return s


def verificar():
    filas = cargar(estados=TODO)
    lunes = [(d, n) for d, n in filas if d.weekday() == 0 and d >= dt.date(2026, 6, 15)]
    v1 = pr = v1h = prh = 0
    for d, real in lunes:
        a = salida_v1(filas, d)["combinado"][:5]
        b = salida(filas, d)["combinado"][:5]
        ha, hb = len(set(real) & set(a)), len(set(real) & set(b))
        v1 += ha >= 2
        pr += hb >= 2
        v1h += ha
        prh += hb
        print(f"{d:%d/%m} {real}  V1 {''.join(a)} ({ha})  proceso {''.join(b)} ({hb})")
    print(f"\nLunes con ≥2 en Top 5: V1 {v1}/{len(lunes)} | proceso {pr}/{len(lunes)} — aciertos {v1h} → {prh}")


def una_fecha(fecha):
    filas = cargar(estados=TODO)
    s = salida(filas, fecha)
    if "regla_lunes" in s:
        print(f"Lunes: dígitos de {s['regla_lunes']} primero")
    print(f"{fecha}: Top 5 {' '.join(s['combinado'][:5])} | Bottom 5 {' '.join(s['combinado'][5:])}")


if __name__ == "__main__":
    una_fecha(dt.date.fromisoformat(sys.argv[1])) if len(sys.argv) > 1 else verificar()
