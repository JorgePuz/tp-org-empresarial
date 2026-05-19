
# =============================================================
# analisis_ventas.py
# Análisis de ventas - TP Organización Empresarial UTN
# =============================================================

import pandas as pd
import matplotlib.pyplot as plt
import os

# Crear carpeta de resultados si no existe
os.makedirs("resultados", exist_ok=True)

# ── Generar dataset de ventas simuladas ──────────────────────
# Se genera el dataset en lugar de leerlo desde un CSV externo
# para garantizar la reproducibilidad en cualquier entorno

data = {
    "id": range(1, 31),
    "fecha": pd.date_range(start="2024-01-01", periods=30, freq="D"),
    "producto": ["Laptop","Mouse","Teclado","Monitor","Laptop",
                 "Mouse","Teclado","Monitor","Laptop","Mouse",
                 "Teclado","Monitor","Laptop","Mouse","Teclado",
                 "Monitor","Laptop","Mouse","Teclado","Monitor",
                 "Laptop","Mouse","Teclado","Monitor","Laptop",
                 "Mouse","Teclado","Monitor","Laptop","Mouse"],
    "cantidad": [1,3,2,1,2,5,1,1,1,4,2,1,3,2,1,2,1,3,2,1,2,4,1,1,1,3,2,1,2,5],
    "precio_unitario": [1200,25,45,300,1200,25,45,300,1200,25,
                        45,300,1200,25,45,300,1200,25,45,300,
                        1200,25,45,300,1200,25,45,300,1200,25]
}

df = pd.DataFrame(data)

# Calcular monto total por fila
# Se multiplica cantidad por precio para obtener el ingreso de cada venta
df["monto"] = df["cantidad"] * df["precio_unitario"]
df["mes"] = df["fecha"].dt.to_period("M")

# Guardar dataset en /datos
df.to_csv("datos/dataset.csv", index=False)
print("Dataset guardado en /datos/dataset.csv")

# ── Indicadores principales ──────────────────────────────────

ventas_totales = df["monto"].sum()
print(f"Ventas totales: ${ventas_totales:,.2f}")

# Producto más vendido (por cantidad total vendida)
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()
print(f"Producto más vendido: {producto_mas_vendido}")

# Ventas por mes (suma de montos agrupados por mes)
ventas_por_mes = df.groupby("mes")["monto"].sum()
print("\nVentas por mes:")
print(ventas_por_mes)

# ── Gráfico de evolución de ventas ──────────────────────────
# Se usa un gráfico de barras para visualizar el monto mensual

plt.figure(figsize=(8, 4))
ventas_por_mes.plot(kind="bar", color="steelblue")
plt.title("Evolución de Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Monto Total ($)")
plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png")
print("\nGráfico guardado en /resultados/grafico_ventas.png")
plt.show()
