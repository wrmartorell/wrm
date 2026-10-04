"""
Proyecto play — Congelar la salida de un día (proceso activo + V2 en paralelo).

Escribe docs/predicciones/AAAA-MM-DD.md usando solo resultados anteriores a la fecha.
Regla fijada (04/10/2026): si después de 20 días ciegos la V2 tiene más días con los
4 dígitos en el Top 7 que el proceso activo, se cambia a la V2.

Uso:
    python3 src/congelar_dia.py 2026-10-05
"""

import datetime as dt
import sys
from pathlib import Path

from proceso import TODO, grupos
from proceso import salida as salida_activo
from v1 import cargar
from v2 import salida as salida_v2

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


def bloque(nombre, filas, fecha, fn):
    comb = fn(filas, fecha)["combinado"]
    lista, total = grupos(filas, fecha, comb)
    L = [f"## {nombre}", "", "```", f"Top 5 {' '.join(comb[:5])} | Bottom 5 {' '.join(comb[5:])}",
         f"Top 7: {' '.join(comb[:7])}", f"Grupos (primeros 35 de {total}):"]
    for i in range(0, 35, 7):
        L.append("  " + "  ".join(f"{i + j + 1:>2}.{g}" for j, g in enumerate(lista[i:i + 7])))
    return L + ["```", ""]


def main(fecha):
    filas = [r for r in cargar(estados=TODO) if r[0] < fecha]
    out = Path(__file__).resolve().parent.parent / "docs" / "predicciones" / f"{fecha.isoformat()}.md"
    if out.exists():
        sys.exit(f"{out.name} ya existe: no se sobrescribe una salida congelada.")
    L = [f"# Salida congelada — {DIAS[fecha.weekday()]} {fecha:%d/%m/%Y}", "",
         f"Datos usados: {filas[0][0]:%d/%m} → {filas[-1][0]:%d/%m/%Y} ({len(filas)} resultados). "
         "Congelada antes de conocer el resultado.", ""]
    L += bloque("Proceso activo", filas, fecha, salida_activo)
    L += bloque("V2 (en paralelo)", filas, fecha, salida_v2)
    L += ["## Resultado real", "", "_Pendiente._", ""]
    out.write_text("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main(dt.date.fromisoformat(sys.argv[1]))
