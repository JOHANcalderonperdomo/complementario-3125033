import pandas as pd
import matplotlib.pyplot as plt

# Datos proporcionados
data = {
    "ID": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ],
    "Metodología": [
        "Agile", "Scrum", "Kanban", "Lean", "XP (Extreme Programming)",
        "DevOps", "Waterfall", "Modelo V", "Desarrollo Incremental", 
        "Desarrollo Basado en Pruebas (TDD)", "Desarrollo Basado en Componentes", 
        "RAD (Rapid Application Development)", "Crystal", 
        "DSDM (Dynamic Systems Development Method)", "FDD (Feature Driven Development)", 
        "SAFE (Scaled Agile Framework)", "Desarrollo Ágil Distribuido", 
        "Continuous Integration (CI)", "Continuous Delivery (CD)", 
        "Modelo Espiral"
    ],
    "Año de Tendencia": [
        2023, 2023, 2022, 2021, 2023, 
        2023, 2020, 2021, 2023, 
        2022, 2022, 2021, 
        2021, 2020, 2023, 
        2023, 2023, 2023, 
        2022, 2021
    ],
    "Popularidad (%)": [
        95, 93, 88, 85, 80, 
        94, 68, 74, 82, 
        89, 84, 76, 
        70, 73, 80, 
        90, 87, 92, 
        90, 79
    ]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Configurar la gráfica de torta
plt.figure(figsize=(12, 12))
plt.pie(
    df["Popularidad (%)"], 
    labels=df["Metodología"], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=plt.cm.Paired.colors, 
    wedgeprops={'edgecolor': 'black'}  # Añadir borde negro a cada segmento
)
plt.title('Popularidad de Metodologías')
plt.axis('equal')  # Asegurar que el gráfico de torta sea circular
plt.tight_layout()  # Ajustar diseño para mejor presentación
plt.show()
