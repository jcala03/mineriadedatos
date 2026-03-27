import pandas as pd
import numpy as np

np.random.seed(42)
N = 600  #Este es el numero dee datps o estudiamtyes

# ─────────────────────────────────────────────
# 1. VARIABLES DEMOGRÁFICAS
# ─────────────────────────────────────────────
edad = np.random.randint(16, 30, size=N).astype(float)
genero = np.random.choice(['Masculino', 'Femenino', 'Otro'], size=N, p=[0.48, 0.50, 0.02])
lugar_origen = np.random.choice(
    ['Barranquilla', 'Soledad', 'Malambo', 'Sabanalarga', 'Otro municipio'],
    size=N, p=[0.45, 0.20, 0.10, 0.10, 0.15]
)

# ─────────────────────────────────────────────
# 2. VARIABLES ACADÉMICAS
# ─────────────────────────────────────────────
promedio_bachillerato = np.round(np.random.normal(3.5, 0.7, size=N).clip(1.0, 5.0), 2)
puntaje_admision      = np.round(np.random.normal(55, 12, size=N).clip(10, 100), 1)
promedio_primer_sem   = np.round(np.random.normal(3.3, 0.8, size=N).clip(0.0, 5.0), 2)

# ─────────────────────────────────────────────
# 3. VARIABLES FINANCIERAS
# ─────────────────────────────────────────────
nivel_socioeconomico = np.random.choice([1, 2, 3, 4, 5, 6], size=N, p=[0.20, 0.30, 0.25, 0.15, 0.07, 0.03])
beca                 = np.random.choice(['Sí', 'No'], size=N, p=[0.35, 0.65])
credito_educativo    = np.random.choice(['Sí', 'No'], size=N, p=[0.25, 0.75])
apoyo_financiero     = np.random.choice(['Ninguno', 'Subsidio', 'Beca parcial', 'Beca completa'],
                                         size=N, p=[0.40, 0.20, 0.25, 0.15])

# ─────────────────────────────────────────────
# 4. VARIABLE OBJETIVO: deserción (lógica realista)
# ─────────────────────────────────────────────
prob_desercion = (
    0.35
    - 0.08 * (promedio_primer_sem - 3.0)
    - 0.05 * (promedio_bachillerato - 3.5)
    - 0.04 * (puntaje_admision - 55) / 10
    + 0.10 * (nivel_socioeconomico <= 2).astype(int)
    - 0.08 * (beca == 'Sí').astype(int)
    - 0.05 * (credito_educativo == 'Sí').astype(int)
    + 0.03 * (edad > 24).astype(int)
).clip(0.05, 0.95)

desercion = np.where(np.random.rand(N) < prob_desercion, 'Sí', 'No')

# ─────────────────────────────────────────────
# 5. CONSTRUIR DATAFRAME BASE
# ─────────────────────────────────────────────
df = pd.DataFrame({
    'edad':                  edad,
    'genero':                genero,
    'lugar_origen':          lugar_origen,
    'promedio_bachillerato': promedio_bachillerato,
    'puntaje_admision':      puntaje_admision,
    'promedio_primer_sem':   promedio_primer_sem,
    'nivel_socioeconomico':  nivel_socioeconomico,
    'beca':                  beca,
    'credito_educativo':     credito_educativo,
    'apoyo_financiero':      apoyo_financiero,
    'desercion':             desercion
})

# ─────────────────────────────────────────────
# 6. INTRODUCIR VALORES NULOS (~5% por columna numérica)
# ─────────────────────────────────────────────
columnas_con_nulos = ['promedio_bachillerato', 'puntaje_admision', 'promedio_primer_sem', 'edad']
for col in columnas_con_nulos:
    idx_nulos = np.random.choice(df.index, size=int(N * 0.05), replace=False)
    df.loc[idx_nulos, col] = np.nan

print(f"Nulos introducidos en: {columnas_con_nulos}")

# ─────────────────────────────────────────────
# 7. INTRODUCIR OUTLIERS (~2% de registros)
# ─────────────────────────────────────────────
n_outliers = int(N * 0.02)

# Outlier alto en puntaje_admision (>100, fuera de rango real)
idx_out_alto = np.random.choice(df[df['puntaje_admision'].notna()].index, size=n_outliers, replace=False)
df.loc[idx_out_alto, 'puntaje_admision'] = np.random.uniform(110, 150, size=n_outliers).round(1)

# Outlier bajo en promedio_primer_sem (valor negativo, imposible)
idx_out_bajo = np.random.choice(df[df['promedio_primer_sem'].notna()].index, size=n_outliers, replace=False)
df.loc[idx_out_bajo, 'promedio_primer_sem'] = np.random.uniform(-2.0, -0.5, size=n_outliers).round(2)

# Outlier en edad (>60, no realista para pregrado)
idx_out_edad = np.random.choice(df[df['edad'].notna()].index, size=n_outliers, replace=False)
df.loc[idx_out_edad, 'edad'] = np.random.randint(65, 90, size=n_outliers).astype(float)

print(f"Outliers introducidos en: puntaje_admision (alto), promedio_primer_sem (bajo), edad (alto)")

# ─────────────────────────────────────────────
# 8. EXPORTAR A CSV
# ─────────────────────────────────────────────
output_path = 'dataset_desercion_estudiantil.csv'
df.to_csv(output_path, index=False, encoding='utf-8-sig', sep=';')

print(f"\n✅ Dataset generado exitosamente: {output_path}")
print(f"   Total registros : {len(df)}")
print(f"   Total columnas  : {len(df.columns)}")
print(f"   Desertores      : {(df['desercion'] == 'Sí').sum()} ({(df['desercion'] == 'Sí').mean()*100:.1f}%)")
print(f"   No desertores   : {(df['desercion'] == 'No').sum()} ({(df['desercion'] == 'No').mean()*100:.1f}%)")
print(f"\nVista previa:")
print(df.head())
print(f"\nResumen de nulos:")
print(df.isnull().sum())
