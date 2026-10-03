# Proyecto de análisis secuencial de números de 4 dígitos

> Documento original del proyecto, transcrito tal cual (solo se adaptó el formato a Markdown).
> La definición exacta y congelada del proceso está en [`version1.md`](version1.md).

## 1. Propósito de este documento

Este archivo consolida todo lo definido, probado, corregido y aprendido hasta este punto para que el proyecto pueda continuar sin perder la línea de trabajo.

La meta no es tratar los resultados como simples apariciones aisladas ni basar el análisis únicamente en frecuencias. La idea central del proyecto es estudiar los números como una secuencia legible, donde cada resultado puede formar parte de una estructura, transformación, ciclo o patrón.

Este documento distingue entre:

- Reglas originales del usuario
- Estructuras matemáticas aceptadas
- Métodos experimentales probados
- Métodos descartados o degradados a "leyenda secundaria"
- Resultados de backtesting
- Método actual
- Protocolo obligatorio para pruebas ocultas

---

## 2. Reglas de trabajo obligatorias

Estas reglas tienen prioridad durante todo el proyecto.

1. No mezclar información de otras conversaciones.
2. Seguir las ideas planteadas por el usuario sin cambiarlas por métodos "tradicionales" por iniciativa propia.
3. No asumir nada importante.
4. Si hace falta cambiar una regla, filtro, fórmula o interpretación, se debe notificar antes.
5. Si algo no se entiende, debe aclararse antes de incorporarlo.
6. Un dato oculto no puede entrar en cálculos, filtros, pesos, selección de fórmula ni ajuste del proceso antes de congelar la predicción.
7. Una vez congelada una predicción histórica:
   - se revela el valor real;
   - se mide el resultado;
   - entonces ese valor puede incorporarse para calcular el siguiente.
8. No corregir una fórmula retroactivamente para hacer que un resultado ya conocido "encaje".
9. Distinguir siempre entre:
   - motor principal;
   - filtros;
   - leyendas/estadísticas secundarias;
   - experimentos todavía no aprobados.
10. El objetivo es leer estructura, no simplemente "adivinar".

---

## 3. Universo de números

La meta son números de cuatro dígitos: **0000 a 9999**.

Total: $10^4 = 10{,}000$

Cada número se representa como **ABCD**, donde:

- A = primer dígito
- B = segundo dígito
- C = tercer dígito
- D = cuarto dígito

Cada unidad pertenece a $\{0,1,2,3,4,5,6,7,8,9\}$.

Ejemplo: 5831 → A=5, B=8, C=3, D=1.

Los ceros a la izquierda son válidos. Ejemplo: 0545 → A=0, B=5, C=4, D=5.

---

## 4. Grupos de Permutación

Se definió que dos números pertenecen al mismo grupo si tienen exactamente los mismos dígitos, sin importar el orden.

Ejemplo: 1234, 4321, 3214, 4123 pertenecen al mismo grupo 1234.

Para representar cada grupo, los dígitos se ordenan de menor a mayor.

Ejemplos:

- 4321 → grupo 1234
- 2143 → grupo 1234
- 3112 → grupo 1123
- 0565 → grupo 0556
- 8230 → grupo 0238
- 0438 → grupo 0348

### 4.1 Cantidad total de grupos

Al agrupar las 10,000 combinaciones por permutación:

$$\binom{10+4-1}{4}=\binom{13}{4}=715$$

Por tanto:

$$10{,}000 \text{ números exactos} \rightarrow 715 \text{ grupos de permutación}$$

Esta reducción es fundamental para el proyecto.

---

## 5. Filtros por presencia de dígitos

Los 715 grupos pueden reducirse si el análisis logra identificar dígitos que necesariamente deben aparecer.

### 5.1 Un dígito confirmado

Si se sabe que aparece un 9, sin importar su posición:

$$715-\binom{12}{4}=715-495=220$$

Por tanto: $715 \rightarrow 220$

**Distribución por cantidad de 9**

Entre esos 220 grupos:

- exactamente un 9 → 165 grupos
- exactamente dos 9 → 45 grupos
- exactamente tres 9 → 9 grupos
- cuatro 9 → 1 grupo (9999)

### 5.2 Dos dígitos distintos confirmados

Si se confirma, por ejemplo, que aparecen 4 y 9: $715 \rightarrow 55$

Los 55 grupos registrados para 4 + 9 fueron:

```
0049, 0149, 0249, 0349, 0449, 0459, 0469, 0479, 0489, 0499
1149, 1249, 1349, 1449, 1459, 1469, 1479, 1489, 1499
2249, 2349, 2449, 2459, 2469, 2479, 2489, 2499
3349, 3449, 3459, 3469, 3479, 3489, 3499
4449, 4459, 4469, 4479, 4489, 4499
4559, 4569, 4579, 4589, 4599
4669, 4679, 4689, 4699
4779, 4789, 4799
4889, 4899
4999
```

### 5.3 Tres dígitos distintos confirmados

Si se confirman tres dígitos distintos, por ejemplo 0,6,7, el cuarto dígito X puede ser cualquiera de 0–9 y quedan 10 grupos:

```
0067, 0167, 0267, 0367, 0467, 0567, 0667, 0677, 0678, 0679
```

Por tanto: $715 \rightarrow 55 \rightarrow 10$

### 5.4 Regla objetivo

Desde temprano se definió como meta:

> **Intentar asegurar al menos dos dígitos del resultado.**

Dos dígitos reducen los 715 grupos a 55 y permiten continuar con filtros posteriores.

---

## 6. Idea secuencial original

La idea inicial no era estudiar números aislados ni solamente frecuencias.

La estructura planteada fue:

$$N_{10}\rightarrow N_9\rightarrow N_8\rightarrow\dots\rightarrow N_1$$

Cada resultado forma parte de la cadena: el más viejo influye en el siguiente, ese en el próximo y así sucesivamente.

La intención es analizar la cadena, no agrupar todos los eventos donde apareció un mismo dígito.

---

## 7. Análisis por posiciones A/B/C/D

Se reafirmó que el análisis debe conservar las posiciones.

Ejemplo: 2337 → 6811 → 0545 → 8173 produce simultáneamente:

- A: 2→6→0→8
- B: 3→8→5→1
- C: 3→1→4→7
- D: 7→1→5→3

Pero estudiar A/B/C/D no debe significar ignorar el número completo.

El proyecto debe conservar ambos niveles: **Número completo** y **A/B/C/D**.

---

## 8. Descubrimiento del ciclo semanal

Se identificó una estructura importante:

- hay resultados de lunes a sábado;
- domingo no tiene número;
- el lunes comienza un nuevo ciclo.

Por tanto, no conviene asumir que sábado→lunes es exactamente el mismo tipo de transición que lunes→martes.

El domingo se trata como una frontera/reset.

Esto creó dos ejes:

### 8.1 Horizontal

Dentro de una misma semana: Lunes → Martes → Miércoles → Jueves → Viernes → Sábado

### 8.2 Vertical

Mismo día entre semanas:

- Lunes₁ → Lunes₂ → Lunes₃ → …
- Martes₁ → Martes₂ → Martes₃ → …

Y así para los seis días.

Nomenclatura acordada:

- Horizontal = recorrido lunes→sábado dentro de la semana.
- Vertical = todos los lunes entre sí, todos los martes entre sí, etc.

---

## 9. Base de datos autoritativa actual

> Versión en datos: [`data/resultados.csv`](../data/resultados.csv).

### 9.1 Regla de interpretación del bloque grande

En el bloque ampliado varias fechas traían cinco dígitos separados. Se tomó como número ABCD los primeros cuatro dígitos. El quinto no se incorporó al número de cuatro dígitos.

### 9.2 Agosto 2026

- Sábado 01 = 6968
- Lunes 03 = 1616
- Martes 04 = 8463
- Miércoles 05 = 4738
- Jueves 06 = 0473
- Viernes 07 = 2286
- Sábado 08 = 0994
- Lunes 10 = 4894
- Martes 11 = 1640
- Miércoles 12 = 3382
- Jueves 13 = 1250
- Viernes 14 = 2548
- Sábado 15 = 9834
- Lunes 17 = 6918
- Martes 18 = 3057
- Miércoles 19 = 3654
- Jueves 20 = 4711
- Viernes 21 = 9533
- Sábado 22 = 5642
- Lunes 24 = 8518
- Martes 25 = 8694
- Miércoles 26 = 9426
- Jueves 27 = 8675
- Viernes 28 = 2542
- Sábado 29 = 0571
- Lunes 31 = 5450

### 9.3 Septiembre 2026

- Martes 01 = 6292
- Miércoles 02 = 3654
- Jueves 03 = 1924
- Viernes 04 = 8325
- Sábado 05 = 7543
- Lunes 07 = 5807
- Martes 08 = 1831
- Miércoles 09 = 4378
- Jueves 10 = 2497
- Viernes 11 = 7942
- Sábado 12 = 6971
- Lunes 14 = 4175
- Martes 15 = 7783
- Miércoles 16 = 6906
- Jueves 17 = 5833
- Viernes 18 = 1971
- Sábado 19 = 6390
- Lunes 21 = 3836
- Martes 22 = 6732
- Miércoles 23 = 2337
- Jueves 24 = 6811
- Viernes 25 = 0545
- Sábado 26 = 8173

### 9.4 Resultados posteriores ya revelados anteriormente

- Lunes 28 = 0565
- Martes 29 = 8230
- Miércoles 30 = 0438

Advertencia: ya son conocidos por el asistente. Pueden usarse para auditoría, pero una prueba futura verdaderamente ciega debe usar un valor todavía no revelado.

### 9.5 Correcciones importantes

La versión autoritativa anterior reemplaza listas tempranas con errores.

Ejemplos:

- Martes 22 = 6732, no 2026.
- Sábado 19 = 6390.
- Las fechas 14–18 quedaron corregidas respecto a una lista inicial desplazada.

Cuando haya conflicto, esta sección manda.

---

## 10. Métodos probados

### 10.1 Método de transiciones por presencia de dígitos ("método antiguo")

Este método preguntaba:

> Cuando aparece un dígito X en un resultado, ¿qué dígitos aparecen en el resultado inmediatamente siguiente?

Si el último resultado era 8173, se estudiaban 8,1,7,3 y se observaba históricamente qué aparecía en el número siguiente.

Una forma de señal era:

$$P(Y|X)\approx\frac{\text{veces que Y apareció después de X}}{\text{veces observadas con X}}$$

Después se combinaban señales para crear un ranking 0–9.

**Problema reconocido**

Este enfoque agrupaba eventos separados y podía perder:

- posiciones A/B/C/D;
- multiplicidad;
- estructura completa de la cadena.

Por eso dejó de considerarse el motor conceptual principal.

**Estado actual**

No se descartó totalmente. Se conserva como motor auxiliar / señal estadística porque en varias pruebas aportó información útil.

---

## 11. Análisis inverso nuevo→viejo

Inicialmente se intentó exigir confirmación en ambas direcciones:

$$\text{Señal válida}=\text{Adelante}\cap\text{Atrás}$$

Después se detectó que esto podía imponer una simetría que los datos no necesariamente tienen.

Interpretación corregida:

- viejo→nuevo puede servir como motor predictivo;
- nuevo→viejo puede servir como diagnóstico;
- no tienen que intersectarse obligatoriamente.

La intersección bidireccional dejó de ser requisito obligatorio.

---

## 12. Filtros experimentales introducidos y retirados

### 12.1 Repetición obligatoria

Se observó que muchos resultados tenían algún dígito repetido.

En una prueba con 0,5,6, imponer repetición redujo a: 0056, 0556, 0566

El real 0565 pertenecía a 0556.

**Problema:** el filtro podía eliminar resultados correctos, por ejemplo 8230, que no tiene repetidos.

**Estado:** **NO es filtro obligatorio.** Puede quedar como leyenda secundaria.

### 12.2 "No compartir dígitos con el anterior"

Se observó en una muestra pequeña que muchas transiciones compartían cero dígitos y se llegó a usar esto para excluir los del último número.

**Problema:** 8230 compartió el 0 con 0565, mostrando que el filtro podía sacar un dígito correcto.

**Estado:** **NO es filtro obligatorio.**

---

## 13. Primera prueba con 28 = 0565

El 28 se excluyó matemáticamente del cálculo y se usaron resultados anteriores hasta 8173.

El método produjo como principales: **0, 6, 5**

El real fue: **0565**

Los tres estaban presentes.

Grupo real: 0565 → 0556

Con el filtro experimental de repetición quedaron: 0056, 0556, 0566, y el grupo real estaba entre los tres.

**Advertencia:** aunque 0565 no entró numéricamente, el asistente ya conocía el resultado. Por tanto no es una prueba completamente ciega.

---

## 14. Prueba del 29 = 8230

Antes de conocerlo se produjeron como principales: **3, 8, 7**

Real: **8230**

Aciertos entre los tres: 8, 3. Dos correctos de tres candidatos.

El grupo real 0238 no sobrevivió a los filtros adicionales. Esto mostró que filtros agresivos podían sacar el real.

---

## 15. Prueba del 30 = 0438

Después de limpiar filtros añadidos se obtuvo un ranking donde estaban muy arriba 6,0,7,3,8....

Real: **0438**

Se observó:

- 0 muy alto;
- 3 y 8 quedaron muy cerca de los primeros puestos;
- 4 muy bajo.

Esto reveló dos problemas:

1. cortar demasiado pronto podía perder señales cercanas;
2. ciertos dígitos reales podían quedar casi invisibles.

---

## 16. Prueba 7 visibles + 7 ocultos

Base inicial:

- 11 = 7942
- 12 = 6971
- 14 = 4175
- 15 = 7783
- 16 = 6906
- 17 = 5833
- 18 = 1971

Ocultos revelados secuencialmente:

- 19 = 6390
- 21 = 3836
- 22 = 6732
- 23 = 2337
- 24 = 6811
- 25 = 0545
- 26 = 8173

Protocolo:

1. predecir;
2. congelar;
3. revelar;
4. incorporar;
5. continuar.

**Resultado usando el método antiguo cronológico**

| Fecha | Real | Aciertos dentro del Top 5 |
|---|---|---:|
| 19 | 6390 | 1 |
| 21 | 3836 | 2 |
| 22 | 6732 | 3 |
| 23 | 2337 | 2 |
| 24 | 6811 | 1 |
| 25 | 0545 | 0 |
| 26 | 8173 | 4 |

El 26 fue muy fuerte: 3,7,8,1 coincidieron con los cuatro dígitos de 8173.

Más tarde se comprobó que ese resultado era muy sensible a cuánta historia se usaba.

---

## 17. Extrapolación posicional A/B/C/D pura

Se probó extrapolar las cuatro secuencias por separado.

| Oculto | Proyección | Real | Dígitos reales detectados |
|---|---|---|---:|
| 19 | 6823 | 6390 | 2 |
| 21 | 5890 | 3836 | 1 |
| 22 | 1990 | 6732 | 0 |
| 23 | 6398 | 2337 | 1 |
| 24 | 3832 | 6811 | 1 |
| 25 | 6714 | 0545 | 1 |
| 26 | 4329 | 8173 | 1 |

Conclusión: **A/B/C/D puro no fue suficiente.**

Las posiciones siguen siendo fundamentales, pero no como única lógica.

---

## 18. Ventanas secuenciales calibradas con 25 y 26

Se exploraron ventanas de tres resultados completos.

Registrado:

- 25 → proyección 5435, real 0545 → 3 de 4 por composición.
- 26 → proyección 7531, real 8173 → 3 de 4 por composición.

Aplicado al 28:

- proyección 1907
- real 0565
- solo coincidió 0

Conclusión: sobreajuste a 25/26; no se conserva como fórmula principal.

---

## 19. Descubrimiento del domingo/reset

Se reorganizó la base por semanas y se distinguió:

- Horizontal: lunes→sábado.
- Vertical: mismo día entre semanas.

El domingo se trata como reset y no como una transición normal sábado→lunes.

---

## 20. Prueba desde 31 de agosto: aprendizaje + reserva

Se ocultó desde lunes 31 de agosto.

Base visible inicial: hasta sábado 29 de agosto.

Se dividió en:

- **Fase 1 — aprendizaje:** 31 de agosto → 12 de septiembre.
- **Fase 2 — reserva:** 14 → 26 de septiembre.

Los resultados reservados no debían influir en ajustes antes de ser medidos.

---

## 21. Motor horizontal puro

En el tramo reservado se registró:

| Fecha | Horizontal | Real | Aciertos |
|---|---:|---:|---:|
| Sep 15 | 0109 | 7783 | 0 |
| Sep 16 | 0220 | 6906 | 1 |
| Sep 17 | 4025 | 5833 | 1 |
| Sep 18 | 0388 | 1971 | 0 |
| Sep 19 | 0900 | 6390 | 2 |
| Sep 22 | 6444 | 6732 | 1 |
| Sep 23 | 5955 | 2337 | 0 |
| Sep 24 | 1264 | 6811 | 2 |
| Sep 25 | 2959 | 0545 | 1 |
| Sep 26 | 5964 | 8173 | 0 |

Resultado: **2 o más dígitos en 2/10.**

Conclusión: **Horizontal puro es débil.**

Se mantiene como leyenda secundaria, no como motor principal.

---

## 22. Motor vertical

Vertical = mismo día entre semanas.

En una prueba reservada 14–26 hubo varios casos con 2 o más dígitos:

- Sep 14 → 2
- Sep 16 → 2
- Sep 19 → 3
- Sep 21 → 2
- Sep 22 → 2
- Sep 25 → 2
- Sep 26 → 2

En ese bloque: **7/12** lograron al menos 2.

En una evaluación posterior sobre un tramo comparable más amplio se registró: **10/24** con al menos 2.

El vertical mostró más estabilidad que el horizontal puro.

---

## 23. Reprueba del método antiguo desde 31 de agosto

Se rescató el método antiguo de transiciones por presencia.

Reglas:

- no vertical;
- no repetición;
- no "no compartir";
- ningún oculto entra antes de congelar la salida.

**Top 4 registrado**

| Fecha | Top 4 | Real | Correctos |
|---|---|---|---:|
| Ago 31 | 4583 | 5450 | 2 |
| Sep 1 | 4852 | 6292 | 1 |
| Sep 2 | 4586 | 3654 | 3 |
| Sep 3 | 4586 | 1924 | 1 |
| Sep 4 | 4586 | 8325 | 2 |
| Sep 5 | 4581 | 7543 | 2 |
| Sep 7 | 4532 | 5807 | 1 |
| Sep 8 | 4582 | 1831 | 1 |
| Sep 9 | 4358 | 4378 | 3 |
| Sep 10 | 4835 | 2497 | 1 |
| Sep 11 | 5483 | 7942 | 1 |
| Sep 12 | 4582 | 6971 | 0 |
| Sep 14 | 4538 | 4175 | 2 |
| Sep 15 | 4587 | 7783 | 2 |
| Sep 16 | 4735 | 6906 | 0 |
| Sep 17 | 4685 | 5833 | 2 |
| Sep 18 | 4758 | 1971 | 1 |
| Sep 19 | 4538 | 6390 | 1 |
| Sep 21 | 4856 | 3836 | 2 |
| Sep 22 | 4378 | 6732 | 2 |
| Sep 23 | 4573 | 2337 | 2 |
| Sep 24 | 7453 | 6811 | 0 |
| Sep 25 | 3487 | 0545 | 1 |
| Sep 26 | 8453 | 8173 | 2 |

**Resumen Top 4**

- 12 de 24 con al menos 2 dígitos.
- 2 de 24 con 3 dígitos.
- 0 con 4.

**Resumen Top 5**

Sin cambiar fórmula, solo ampliando lectura:

- 15 de 24 con al menos 2.
- 6 de 24 con al menos 3.
- 0 con 4.

$15/24=62.5\%$ para al menos dos dígitos.

**Hallazgo importante**

El caso espectacular del 26, que antes dio 3,7,8,1, no se reprodujo usando todo agosto.

Con toda la historia, el 26 produjo 8,4,5,3 y acertó 8,3.

Esto muestra que el método antiguo es muy sensible a la longitud de la ventana histórica.

---

## 24. Combinación por intersección: antiguo + vertical

Se probó:

$$\text{Candidato}=\text{Antiguo}\cap\text{Vertical}$$

Resultado: solo 4 de 24 lograron al menos 2 dígitos dentro de la intersección.

Conclusión: **NO usar intersección como filtro obligatorio**, porque un motor puede ver información que el otro no ve.

---

## 25. Combinación actual: suma de evidencia

Se cambió la combinación.

Regla:

> Un dígito encontrado por ambos motores recibe prioridad alta, pero un dígito visto solo por uno **no se elimina**.

Sin pesos complejos, el orden conceptual fue:

1. coincidencias entre ambos → mayor respaldo;
2. candidatos restantes del método antiguo;
3. candidatos verticales faltantes;
4. nadie se elimina solo porque el otro motor no lo vea.

**Resultado Top 5 combinado**

Sobre 24 pruebas:

- 16 de 24 con al menos 2 dígitos.
- 6 de 24 con al menos 3 dígitos.
- 1 de 24 con los 4 dígitos reales dentro del Top 5.

$16/24\approx66.7\%$ para al menos 2.

$6/24=25\%$ para al menos 3.

**Caso de 4 dígitos**

9 de septiembre:

- Método antiguo: 4,3,5,8
- Vertical: 7,8,8,2
- Combinado Top 5: 8,4,3,5,7
- Real: 4378

Los cuatro reales estaban dentro del Top 5: 4,3,7,8.

Este es el mejor resultado registrado hasta ahora del enfoque combinado.

---

## 26. Método actual

**Motor A — método antiguo**

Transiciones históricas por presencia de dígitos.

Uso actual: motor auxiliar de señal/ranking.

Preferencia registrada: **Top 5**, porque ha dado la cobertura histórica más útil entre los cortes evaluados.

**Motor B — vertical**

Mismo día de semana entre ciclos:

- lunes con lunes;
- martes con martes;
- miércoles con miércoles;
- jueves con jueves;
- viernes con viernes;
- sábado con sábado.

Respeta el domingo como reset.

**Combinación:** **Suma de evidencia.** No intersección obligatoria.

Un candidato visto en ambos sube de prioridad. Uno visto por un solo motor sigue vivo.

**Horizontal:** permanece como señal secundaria/leyenda.

**Grupos de Permutación:** se usan después de identificar dígitos con respaldo.

- Dos dígitos: $715\rightarrow55$
- Tres dígitos: $55\rightarrow10$

La reducción no debe hacerse con filtros que no hayan demostrado estabilidad.

---

## 27. Leyenda secundaria

Se conservan como información de apoyo, no como filtros automáticos:

- frecuencia global de dígitos;
- transiciones históricas X→Y;
- repetición de dígitos;
- cantidad de dígitos compartidos con el anterior;
- horizontal de la semana;
- otros patrones estadísticos auxiliares.

Pueden ayudar a:

- desempatar;
- ordenar Top 5;
- estudiar por qué un motor ve X y otro Y.

No deben eliminar candidatos sin aprobación explícita.

---

## 28. Qué NO hacer

1. No volver a convertir repetición en regla obligatoria.
2. No volver a eliminar automáticamente dígitos porque aparecieron en el resultado anterior.
3. No exigir que viejo→nuevo y nuevo→viejo coincidan.
4. No usar horizontal puro como motor principal.
5. No construir una fórmula mirando primero el valor oculto.
6. No usar una fecha oculta para escoger cuál método "funciona".
7. No declarar válida una fórmula solo porque acierte uno o dos casos.
8. No ignorar el domingo/reset.
9. No perder A/B/C/D por convertir todo en un simple conjunto.
10. No perder el número completo por analizar solamente sus dígitos.

---

## 29. Protocolo obligatorio de backtesting

**Paso 1 — corte temporal**

Elegir fecha objetivo T. Solo se permite usar $N_1,\dots,N_{T-1}$.

**Paso 2 — congelar**

Antes de revelar T, guardar:

- ranking del motor antiguo;
- salida vertical;
- salida horizontal si se desea como leyenda;
- Top combinado;
- dígitos principales;
- grupos de permutación resultantes;
- cualquier cálculo A/B/C/D.

**Paso 3 — revelar**

Solo después: $N_T=ABCD$

**Paso 4 — medir**

Registrar:

- Top 4;
- Top 5;
- rango de cada dígito real;
- si el grupo real sobrevivió;
- si A/B/C/D fueron correctos;
- qué motor aportó cada acierto.

**Paso 5 — incorporar**

Después de medir, T puede entrar al historial y se pasa a T+1.

**Paso 6 — ajustes**

Un cambio de fórmula debe:

1. justificarse con varios casos;
2. definirse antes de usar el siguiente oculto;
3. quedar documentado;
4. no corregir retroactivamente predicciones anteriores.

---

## 30. Métricas recomendadas

No medir solamente "acertó/no acertó".

**Cobertura de dígitos**

$$C_k=\frac{\#\text{ dígitos reales presentes en Top }k}{4}$$

Ejemplo: si Top 5 contiene 3 de los cuatro reales: $C_5=\frac34=75\%$

**Precisión del conjunto candidato**

Si Top 5 tiene 3 reales: $P_5=\frac35=60\%$

**Supervivencia de grupo**

$$G=\begin{cases}1,&\text{si el grupo real está entre los candidatos}\\0,&\text{si no}\end{cases}$$

**Posiciones A/B/C/D**

Medir por separado:

- acierto de A;
- acierto de B;
- acierto de C;
- acierto de D.

**Ranking de los dígitos reales**

Para cada dígito real, registrar en qué lugar apareció en el ranking 0–9.

Esto permite diferenciar:

- error de señal;
- error de corte;
- error de ordenamiento.

---

## 31. Preguntas abiertas principales

### 31.1 Longitud óptima de la ventana histórica

El método antiguo cambió mucho según se usó historia corta o toda la historia.

Debe probarse, sin cambiar fórmula:

- últimos 6 resultados;
- últimos 12;
- últimos 18;
- historia completa.

La longitud de ventana puede ser una variable crítica.

### 31.2 Cómo integrar A/B/C/D correctamente

A/B/C/D puro falló, pero las posiciones no deben abandonarse.

Se debe investigar $ABCD_t\rightarrow ABCD_{t+1}$ sin reducirlo únicamente a cuatro extrapolaciones independientes.

### 31.3 Qué aporta realmente el reset del domingo

El vertical funciona mejor que el horizontal puro.

Debe estudiarse si:

- lunes tiene comportamiento especial;
- sábado cierra una estructura;
- la semana completa genera un "estado" que condiciona el lunes siguiente.

### 31.4 Cómo convertir Top 5 en grupos útiles

El objetivo futuro es pasar de **Top 5 de dígitos** hacia **2–3 dígitos de alta confianza** para luego:

$$715\rightarrow55\rightarrow10\rightarrow\text{grupo(s) final(es)}$$

sin eliminar el grupo real.

### 31.5 Cómo tratar señales casi empatadas

Ejemplo registrado:

- 7 = 0.329
- 3 = 0.321
- 8 = 0.320

No debe interpretarse 7 como claramente superior.

Deben contemplarse:

- empates;
- bandas de señal;
- candidatos estadísticamente cercanos.

---

## 32. Estado de los métodos

| Método | Estado |
|---|---|
| Secuencia cronológica completa | **Fundamental** |
| A/B/C/D | **Fundamental; falta mejorar integración** |
| Grupos de permutación | **Fundamental** |
| Domingo como reset | **Fundamental** |
| Vertical por día de semana | **Motor activo** |
| Método antiguo de transiciones | **Motor activo/auxiliar** |
| Suma de evidencia | **Combinación actual** |
| Top 5 | **Lectura actual preferida** |
| Horizontal dentro de semana | **Leyenda secundaria** |
| Frecuencias | **Leyenda secundaria** |
| Repetición obligatoria | **Descartada como filtro** |
| No compartir con anterior | **Descartada como filtro** |
| Intersección viejo↔nuevo | **Descartada como obligación** |
| Intersección antiguo∩vertical | **Descartada como filtro** |
| A/B/C/D por extrapolación pura | **No funcionó como motor único** |
| Ventanas de 3 calibradas | **Sobreajuste; no usar como fórmula principal** |

---

## 33. Mejor resultado cuantitativo registrado hasta ahora

Con **Método antiguo Top 5 + vertical como suma de evidencia** se registró:

- **16/24 = 66.7%** de pruebas con al menos 2 dígitos reales dentro del Top 5.
- **6/24 = 25%** con al menos 3 dígitos.
- **1/24** con los cuatro dígitos reales dentro del Top 5.

Esto no significa que exista todavía una probabilidad demostrada de acertar el próximo resultado. Es el desempeño histórico registrado de ese método en esas pruebas.

---

## 34. Próximo experimento recomendado

Sin cambiar la fórmula actual:

**Experimento A — ventanas históricas**

Correr exactamente el mismo motor antiguo con:

- ventana 6;
- ventana 12;
- ventana 18;
- historia completa.

En paralelo mantener el vertical.

Para cada fecha oculta:

1. generar los cuatro rankings antiguos;
2. generar vertical;
3. combinar por suma de evidencia;
4. medir cobertura y posiciones dentro del Top 5;
5. determinar qué ventana mantiene mejor desempeño fuera de muestra.

Importante: la ventana ganadora debe escogerse en un bloque de aprendizaje y después congelarse para un bloque reservado.

---

## 35. Filosofía de continuidad

La línea del proyecto es:

$$\text{Secuencia} + \text{estructura semanal} + \text{A/B/C/D} + \text{grupos de permutación} + \text{evidencia acumulada}$$

No se busca depender de una sola estadística ni asumir que una coincidencia aislada demuestra un patrón.

El objetivo es encontrar una estructura que:

1. pueda definirse antes de conocer el resultado;
2. sobreviva múltiples pruebas ocultas;
3. conserve al menos 2 dígitos con suficiente frecuencia;
4. permita reducir los 715 grupos sin eliminar sistemáticamente el grupo real;
5. sea reproducible.

---

## 36. Regla final para continuar desde este archivo

Cuando se retome el proyecto:

1. cargar esta metodología;
2. usar la base autoritativa;
3. no traer métodos externos sin avisar;
4. respetar ocultamiento temporal;
5. mantener resultados por motor separados;
6. combinar por suma de evidencia, no por eliminación;
7. documentar cualquier cambio antes de probarlo;
8. no usar resultados ocultos hasta haber congelado la salida;
9. seguir midiendo el Top 5 y la posición de los dígitos reales fuera de él;
10. continuar buscando una lectura que transforme candidatos de dígitos en grupos de permutación útiles.

---

*Fin del estado actual del proyecto. Documento preparado para conservar la continuidad del análisis y evitar repetir errores metodológicos ya identificados.*

---

## 37. Nueva línea de análisis: Top 5 y ubicación de los dígitos faltantes

### 37.1 Reconstrucción exacta del combinado que produjo 16/24

Se verificó nuevamente la fórmula que reproduce exactamente los resultados históricos registrados:

- 16/24 con mínimo 2 dígitos reales;
- 6/24 con mínimo 3;
- 1/24 con los 4 dígitos distintos dentro del Top 5.

La construcción exacta del ranking combinado fue:

1. Calcular el ranking completo del método antiguo.
2. Tomar sus Top 4 iniciales.
3. Calcular la proyección vertical del mismo día de semana.
4. Extraer los dígitos distintos de la proyección vertical.
5. Colocar primero los dígitos que aparecen tanto en el Top 4 antiguo como en vertical.
6. Añadir los demás dígitos del Top 4 antiguo manteniendo su orden.
7. Añadir los dígitos verticales que todavía no aparecieron.
8. Completar las posiciones restantes con el ranking completo del método antiguo.
9. El Top 5 combinado son los primeros cinco dígitos de ese ranking completo.

Esta definición reproduce exactamente las métricas históricas anteriores y debe usarse como referencia autoritativa para ese combinado.

### 37.2 Dónde están los dígitos reales que Top 5 deja fuera

Se añade una nueva métrica obligatoria:

> Para cada resultado real, registrar la posición exacta (#6–#10) de todo dígito real que no haya quedado dentro del Top 5.

En las 16 pruebas donde el Top 5 ya contenía al menos 2 dígitos reales, las apariciones de dígitos reales faltantes se distribuyeron así:

- posición #6 → 4 apariciones
- posición #7 → 6 apariciones
- posición #8 → 2 apariciones
- posición #9 → 4 apariciones
- posición #10 → 3 apariciones

Las posiciones #6 y #7 concentran $10/19 \approx 52.6\%$ de las apariciones faltantes registradas en esos casos, pero existe señal real también en #8–#10.

**En los 10 casos con exactamente 2 dígitos dentro del Top 5**

Los dígitos reales faltantes aparecieron:

- #6 → 4 veces
- #7 → 6 veces
- #8 → 2 veces
- #9 → 3 veces
- #10 → 2 veces

**En los 5 casos con 3 dígitos dentro del Top 5**

En varios casos el cuarto dígito era una repetición de uno ya encontrado, por lo que todos los dígitos distintos ya estaban representados.

Cuando realmente faltó un cuarto dígito distinto, apareció muy abajo (#9 o #10).

### 37.3 Estado actual después de esta prueba

- Top 5 sigue siendo la cobertura principal y el foco actual.
- Se mantiene la métrica histórica de:
  - 16/24 con mínimo 2 dígitos;
  - 6/24 con mínimo 3;
  - 1/24 con los 4 dígitos distintos dentro del Top 5.
- Se añade obligatoriamente el seguimiento de la posición #6–#10 de los dígitos reales que queden fuera.
- No se introduce ningún recorte adicional dentro del Top 5.
- La próxima línea de investigación debe centrarse en entender por qué algunos dígitos reales quedan en #6–#10 y cómo usar esa información sin destruir la cobertura del Top 5.

---

## 38. Resultado de la prueba con Bottom 5 y escenarios de rescate

### 38.1 Comparación Top 5 vs Bottom 5

Sobre las mismas 24 pruebas históricas:

**Top 5**

- 16/24 con mínimo 2 dígitos reales.
- 6/24 con mínimo 3 dígitos reales.
- 1/24 con los 4 dígitos reales.
- 47 aciertos acumulados.

**Bottom 5 (#6–#10)**

- 15/24 con mínimo 2 dígitos reales.
- 3/24 con mínimo 3 dígitos reales.
- 0/24 con los 4 dígitos reales.
- 38 aciertos acumulados.

Conclusión: **Top 5 sigue siendo superior como base principal**, pero **Bottom 5 contiene señal real y no debe ignorarse**.

### 38.2 Distribución total de dígitos reales fuera del Top 5

Sumando todos los casos analizados, las posiciones donde aparecieron dígitos reales que quedaron fuera del Top 5 fueron:

- #6 → 7 veces
- #7 → 9 veces
- #8 → 7 veces
- #9 → 8 veces
- #10 → 7 veces

La posición más frecuente fue #7, seguida por #9.

Sin embargo, la distribución es suficientemente repartida como para no justificar rescatar siempre una posición fija.

### 38.3 Distribución según cuánto acertó el Top 5

| Aciertos del Top 5 | Casos | #6 | #7 | #8 | #9 | #10 |
|---|---:|---:|---:|---:|---:|---:|
| 1 acierto | 8 | 3 | 3 | 5 | 4 | 4 |
| 2 aciertos | 10 | 4 | 6 | 2 | 3 | 2 |
| 3 aciertos | 5 | 0 | 0 | 0 | 1 | 1 |
| 4 aciertos | 1 | 0 | 0 | 0 | 0 | 0 |

Lectura:

- Cuando Top 5 acertó solo 1, los faltantes se desplazaron más hacia #8–#10.
- Cuando Top 5 acertó 2, los faltantes se concentraron más en #6–#7.
- Cuando Top 5 acertó 3, los pocos dígitos distintos faltantes aparecieron muy abajo (#9–#10).

Esto es útil para diagnóstico, pero todavía no permite decidir antes del resultado qué zona rescatar.

### 38.4 Prueba con cuatro escenarios de rescate

Se probaron cuatro escenarios distintos construidos a partir de:

- Top 5 combinado;
- Bottom 5;
- comportamiento histórico de las posiciones #6–#10.

Los cuatro escenarios se evaluaron históricamente ocultando cada resultado antes de medirlo.

Resultado conjunto:

- en 21/24 casos, al menos uno de los cuatro escenarios logró mínimo 2 dígitos;
- en 7/24, al menos uno logró mínimo 3 dígitos;
- ninguno mejoró de forma estable hasta 4 dígitos.

Importante: **Los cuatro escenarios no reemplazan al Top 5.**

Su mejora aparente ocurre en parte porque, entre los cuatro conjuntos, se cubre una porción muy grande de los 10 dígitos posibles.

Por tanto, esta prueba se conserva como **diagnóstico y aprendizaje** y no como nueva fórmula oficial.

### 38.5 Estado oficial después de esta prueba

Se mantiene: **Top 5 combinado = base principal.**

Se conserva: **Bottom 5 = segunda fuente de señal**, pero sin usarlo todavía como filtro automático.

Los cuatro escenarios de rescate:

- no se descartan como información;
- no se consideran una mejora oficial;
- no sustituyen al Top 5;
- sirven para entender cómo se distribuye la señal fuera del corte principal.

La siguiente meta sigue siendo:

> Encontrar una condición disponible **antes de conocer el resultado** que permita saber cuándo confiar en el Top 5 y cuándo existe una señal relevante en el Bottom 5.

---

## 39. Regla de los dos valores anteriores por posición — experimento descartado

### 39.1 Idea probada

Se evaluó una regla posicional adicional:

> Para cada posición A/B/C/D, observar los dos valores inmediatamente anteriores de esa misma posición y evitar reutilizarlos en la siguiente fecha.

Ejemplo:

- día 1: A = 7
- día 2: A = 8
- siguiente fecha: penalizar 7 y 8 en A

La intención era utilizar la persistencia posicional para reducir candidatos dentro de A/B/C/D.

### 39.2 Primera prueba histórica

Aplicada secuencialmente sobre 24 casos, la regla mostró inicialmente:

- 84/96 posiciones reales no utilizaron ninguno de los dos valores anteriores.
- A respetó la regla en 22/24.
- B en 21/24.
- C en 19/24.
- D en 22/24.

Integrada al proceso completo, produjo una mejora histórica aparente:

- mínimo 2 posiciones correctas: 17/24 → 19/24
- mínimo 3 posiciones correctas: 9/24 → 11/24
- 4 posiciones correctas: 4/24 → 4/24
- aciertos posicionales totales: 54/96 → 57/96

Sin embargo, esa prueba podía estar afectada por el hecho de que la regla fue diseñada después de haber observado resultados históricos.

### 39.3 Versión fortalecida sin usar los 24 ocultos para definir la regla

Para reducir contaminación, la regla fue reconstruida utilizando únicamente datos anteriores al 31 de agosto.

La exclusión de los dos valores anteriores solo se permitiría en transiciones y posiciones donde la historia previa mostrara suficiente respaldo.

La versión congelada produjo:

- aciertos posicionales totales: 57/96
- mínimo 2 posiciones: 19/24
- mínimo 3 posiciones: 10/24
- las 4 posiciones: 5/24

A pesar de esa mejora histórica, al aplicarla al jueves 1 de octubre redujo la calidad de la lectura respecto al proceso anterior.

### 39.4 Resultado en el jueves 1 de octubre

Antes de incorporar esta capa, uno de los escenarios ya había logrado una lectura con 3 dígitos correctos.

Con la capa de los dos valores anteriores, incluso en su versión fortalecida, el mejor resultado potencial cayó a solamente 2 dígitos.

Esto mostró que la regla podía:

- mejorar ciertos backtests históricos;
- pero interferir con señales útiles del proceso principal;
- reducir candidatos correctos en un caso nuevo.

### 39.5 Decisión final

La regla de los dos valores anteriores queda: **DESCARTADA DEL PROCESO ACTIVO.**

No debe:

- modificar el Top 5;
- modificar Bottom 5;
- penalizar A/B/C/D;
- eliminar candidatos;
- alterar futuros rankings.

Se conserva únicamente como **experimento documentado** para referencia histórica.

---

## 40. Estado oficial del proceso después de descartar esta capa

El proceso activo vuelve al estado anterior a la regla de los dos valores previos.

Se mantiene:

1. Top 5 combinado como base principal.
2. Método antiguo como una de las fuentes de señal.
3. Vertical por día de semana como segunda fuente estructural.
4. Suma de evidencia, no intersección obligatoria.
5. Bottom 5 como segunda fuente de señal para diagnóstico y posible rescate futuro.
6. Distribución histórica de los dígitos reales en posiciones #6–#10.
7. Los cuatro escenarios de rescate únicamente como diagnóstico, no como fórmula oficial.
8. A/B/C/D como estructura importante, pero sin la regla de exclusión de los dos valores anteriores.
9. Domingo como reset.
10. Protocolo estricto de ocultamiento secuencial para pruebas futuras.

No se incorpora ninguna penalización nueva por posición hasta que una regla futura demuestre mejora sin destruir señales existentes.
