# play

Análisis secuencial de números de 4 dígitos (0000–9999).

- [`docs/metodologia.md`](docs/metodologia.md) — documento del proyecto: reglas, métodos probados, resultados y protocolo.
- [`docs/version1.md`](docs/version1.md) — **Versión 1 congelada**: fórmulas exactas y verificación.
- [`data/resultados.csv`](data/resultados.csv) — base de datos autoritativa.
- [`src/v1.py`](src/v1.py) — implementación congelada de la Versión 1.
- [`docs/proceso_activo.md`](docs/proceso_activo.md) / [`src/proceso.py`](src/proceso.py) — **proceso activo** (V1 + regla del lunes).

## Uso

```
python3 src/v1.py
```

Reproduce el backtest 31/08 → 26/09/2026: Top 4 antiguo 24/24 igual al registrado; Top 5 combinado 16/24 (≥2), 6/24 (≥3), 1/24 (4).

Requiere solo Python 3.
