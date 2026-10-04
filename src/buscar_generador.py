"""
Proyecto play — Búsqueda exhaustiva de una regla generadora.

Si los números salen de un proceso con estructura, debe existir una regla
x_t = f(resultados anteriores). Se prueban familias completas de reglas
y cada regla se escoge SOLO con jun-jul y se mide en ago-oct (fechas que no
participaron en la elección).

Familias:
 1) Por posición: x_t[p] = (a·x_{t-1}[q] + b·x_{t-2}[r] + c) mod 10
    (a, b, c de 0 a 9; q, r cualquier posición A/B/C/D) → 16,000 reglas por posición.
 2) Número completo: N_t = (a·N_{t-1} + c) mod 10000 (a de 0 a 9999).
"""
import datetime as dt
from collections import Counter
from v1 import cargar

f = cargar(estados=("historico_previo", "autoritativo"))
N = [n for _, n in f]
D = [d for d, _ in f]
corte = next(i for i, d in enumerate(D) if d >= dt.date(2026, 8, 1))
P = "ABCD"

print("1) Reglas por posición (elegida en jun-jul, medida en ago-oct)")
for p in range(4):
    mejor = None
    for q in range(4):
        for r in range(4):
            for a in range(10):
                for b in range(10):
                    pares = [(int(N[i-1][q]), int(N[i-2][r]), int(N[i][p])) for i in range(2, corte)]
                    cs = Counter((y - a*x1 - b*x2) % 10 for x1, x2, y in pares)
                    c, k = cs.most_common(1)[0]
                    if mejor is None or k > mejor[0]:
                        mejor = (k, a, q, b, r, c)
    k, a, q, b, r, c = mejor
    ok = sum((a*int(N[i-1][q]) + b*int(N[i-2][r]) + c) % 10 == int(N[i][p]) for i in range(corte, len(N)))
    print(f"  {P[p]} = {a}·ayer[{P[q]}] + {b}·anteayer[{P[r]}] + {c} (mod 10): "
          f"jun-jul {k}/{corte-2} ({100*k/(corte-2):.0f}%) → ago-oct {ok}/{len(N)-corte} ({100*ok/(len(N)-corte):.0f}%)")

print("\n2) Número completo N_t = a·N_(t-1) + c (mod 10000)")
mejor = None
for a in range(10000):
    cs = Counter((int(N[i]) - a*int(N[i-1])) % 10000 for i in range(1, corte))
    c, k = cs.most_common(1)[0]
    if mejor is None or k > mejor[0]:
        mejor = (k, a, c)
k, a, c = mejor
ok = sum((a*int(N[i-1]) + c) % 10000 == int(N[i]) for i in range(corte, len(N)))
print(f"  mejor: a={a}, c={c}: jun-jul {k}/{corte-1} → ago-oct {ok}/{len(N)-corte}")
