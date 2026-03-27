# Dataset Sintético — Deserción Estudiantil

**Curso:** Minería de Datos  
**Universidad:** Universidad de la Costa (CUC)  
**Actividad:** Actividad I — Supervised vs Unsupervised Learning  
**Docente:** José Escorcia-Gutierrez, Ph.D.

---

## Descripción del Dataset

Este dataset sintético simula información de estudiantes universitarios durante su primer año académico, con el objetivo de predecir si un estudiante desertará o no de su programa de pregrado.

**Archivo:** `dataset_desercion_estudiantil.csv`  
**Total de registros:** 600  
**Total de variables:** 11

---

## Descripción de Variables

| Variable | Tipo | Rango / Categorías | Descripción |
|---|---|---|---|
| `edad` | Numérica (int) | 16 – 29 (con outliers hasta 90) | Edad del estudiante al momento de ingreso |
| `genero` | Categórica | Masculino, Femenino, Otro | Género del estudiante |
| `lugar_origen` | Categórica | Barranquilla, Soledad, Malambo, Sabanalarga, Otro municipio | Municipio de procedencia |
| `promedio_bachillerato` | Numérica (float) | 1.0 – 5.0 | Promedio académico en educación media |
| `puntaje_admision` | Numérica (float) | 10 – 100 (con outliers hasta 150) | Puntaje obtenido en la prueba de admisión |
| `promedio_primer_sem` | Numérica (float) | 0.0 – 5.0 (con outliers negativos) | Promedio académico del primer semestre |
| `nivel_socioeconomico` | Numérica (int) | 1 – 6 | Estrato socioeconómico del estudiante |
| `beca` | Categórica | Sí, No | Indica si el estudiante tiene beca |
| `credito_educativo` | Categórica | Sí, No | Indica si el estudiante tiene crédito educativo (ej. ICETEX) |
| `apoyo_financiero` | Categórica | Ninguno, Subsidio, Beca parcial, Beca completa | Tipo de apoyo financiero recibido |
| `desercion` | Categórica (objetivo) | Sí, No | Variable objetivo: indica si el estudiante desertó |

---

## Valores Nulos

Se introdujeron valores nulos de forma aleatoria en las siguientes columnas numéricas, representando aproximadamente el **5% de los registros** por columna:

| Columna | % de nulos aproximado |
|---|---|
| `edad` | ~5% |
| `promedio_bachillerato` | ~5% |
| `puntaje_admision` | ~5% |
| `promedio_primer_sem` | ~5% |

**Justificación:** Los valores nulos simulan situaciones reales como registros incompletos en sistemas académicos, estudiantes que no reportaron su edad o cuyos datos de bachillerato no fueron digitalizados.

---

## Outliers

Se introdujeron valores atípicos en un **~2% de los registros** por columna afectada:

| Columna | Tipo de outlier | Rango del outlier | Justificación |
|---|---|---|---|
| `puntaje_admision` | Alto (por encima del máximo real) | 110 – 150 | Simula errores de digitación o datos corruptos |
| `promedio_primer_sem` | Bajo (valores negativos, imposibles) | -2.0 – -0.5 | Simula errores de captura en sistemas de notas |
| `edad` | Alto (edades no realistas para pregrado) | 65 – 90 | Simula registros con fecha de nacimiento incorrecta |

---

## Lógica de Generación de la Variable Objetivo

La probabilidad de deserción de cada estudiante fue calculada con la siguiente lógica:

- Mayor probabilidad si el `promedio_primer_sem` es bajo
- Mayor probabilidad si el `nivel_socioeconomico` es 1 o 2
- Menor probabilidad si tiene `beca = Sí` o `credito_educativo = Sí`
- Ligero aumento si la `edad` es mayor de 24 años

Esta lógica refleja factores de riesgo reales identificados en literatura sobre deserción universitaria en Colombia.

---

## Cómo reproducir el dataset

```bash
# Instalar dependencias
pip install pandas numpy

# Ejecutar el script
python generar_dataset.py
```

---

## Integrantes del grupo

| Nombre | 
|---|
| Cala Ardila Jhonny Gabriel
| Ramos Amador Antwan

