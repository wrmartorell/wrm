"""
Proyecto play — Experimento A: ventanas históricas del motor antiguo.

Usa la Versión 1 (src/v1.py) sin modificarla. Lo único que cambia es la
historia que recibe el motor antiguo.

Definiciones aprobadas antes de correr:
- Ventana N = últimos N resultados antes de la fecha objetivo (N−1 transiciones).
  Si hay menos de N resultados disponibles, se usa toda la historia disponible.
- Ventanas: 6, 12, 18 e historia completa (= V1).
- Vertical y combinado: exactamente como V1.
- Aprendizaje: 15/08 → 29/08/2026 (13 fechas).
- Reserva: 31/08 → 26/09/2026 (24 fechas).
- Criterio de la ganadora (solo en aprendizaje): más fechas con ≥2 dígitos reales
  en el Top 5 combinado; empate → más aciertos totales; empate → historia completa.

Uso:
    python3 src/experimento_a.py
"""

import datetime as dt

from v1 import cargar, combinado, motor_antiguo, motor_vertical

VENTANAS = [6, 12, 18, None]  # None = historia completa
APRENDIZAJE = (dt.date(2026, 8, 15), dt.date(2026, 8, 29))
RESERVA = (dt.date(2026, 8, 31), dt.date(2026, 9, 26))


def nombre(v):
    return "completa" if v is None else f"ventana {v}"


def salida_ventana(filas, fecha, ventana):
    historia = [n for d, n in filas if d < fecha]
    if ventana is not None:
        historia = historia[-ventana:]
    ranking, _ = motor_antiguo(historia)
    return combinado(ranking, motor_vertical(filas, fecha))


def evaluar(filas, ventana, bloque):
    desde, hasta = bloque
    m = {"n": 0, "ge2": 0, "ge3": 0, "c4": 0, "aciertos": 0,
         "fuera": {k: 0 for k in range(6, 11)}, "detalle": []}
    for fecha, real in [(d, n) for d, n in filas if desde <= d <= hasta]:
        comb = salida_ventana(filas, fecha, ventana)
        top5 = comb[:5]
        h = len(set(real) & set(top5))
        m["n"] += 1
        m["aciertos"] += h
        m["ge2"] += h >= 2
        m["ge3"] += h >= 3
        m["c4"] += h >= 4
        for x in set(real):
            r = comb.index(x) + 1
            if r > 5:
                m["fuera"][r] += 1
        m["detalle"].append((fecha, real, "".join(top5), h))
    return m


def imprimir(titulo, resultados):
    print(f"\n{titulo}")
    print(f"{'motor antiguo':<14} {'≥2':>6} {'≥3':>6} {'4':>5} {'aciertos':>9}   fuera del Top 5 (#6..#10)")
    for v, m in resultados.items():
        n = m["n"]
        fuera = " ".join(f"{m['fuera'][k]}" for k in range(6, 11))
        print(f"{nombre(v):<14} {m['ge2']:>3}/{n:<2} {m['ge3']:>3}/{n:<2} {m['c4']:>2}/{n:<2} {m['aciertos']:>9}   {fuera}")


def main():
    filas = cargar()

    # 1) Aprendizaje: escoger ventana solo con estas fechas.
    apr = {v: evaluar(filas, v, APRENDIZAJE) for v in VENTANAS}
    imprimir("APRENDIZAJE 15/08 → 29/08 (13 fechas)", apr)
    orden = sorted(VENTANAS, key=lambda v: (-apr[v]["ge2"], -apr[v]["aciertos"], v is not None))
    ganadora = orden[0]
    print(f"\nVentana ganadora (congelada antes de la reserva): {nombre(ganadora)}")

    # 2) Reserva: se mide la ganadora; las demás se muestran solo como referencia.
    res = {v: evaluar(filas, v, RESERVA) for v in VENTANAS}
    imprimir("RESERVA 31/08 → 26/09 (24 fechas)", res)
    print(f"\nGanadora en reserva ({nombre(ganadora)}): "
          f"≥2 {res[ganadora]['ge2']}/24, ≥3 {res[ganadora]['ge3']}/24, "
          f"4 {res[ganadora]['c4']}/24, aciertos {res[ganadora]['aciertos']}")

    print("\nDETALLE RESERVA — Top 5 combinado y aciertos por ventana")
    print("fecha       real  " + "  ".join(f"{nombre(v):>13}" for v in VENTANAS))
    for i, (fecha, real, _, _) in enumerate(res[None]["detalle"]):
        celdas = "  ".join(f"{res[v]['detalle'][i][2]} ({res[v]['detalle'][i][3]})".rjust(13) for v in VENTANAS)
        print(f"{fecha}  {real}  {celdas}")


if __name__ == "__main__":
    main()
