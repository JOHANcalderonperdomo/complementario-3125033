import pandas as pd
import matplotlib.pyplot as plt

# Datos proporcionados
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "Arquitectura": [
        "Microservicios", "Monolítica", "Serverless", 
        "Arquitectura Orientada a Eventos", "SOA (Arquitectura Orientada a Servicios)", 
        "CQRS", "Lambda", "Arquitectura Hexagonal", "Event Sourcing", 
        "Clean Architecture", "Arquitectura REST", "Arquitectura de Capas", 
        "Micro Frontends", "Event-driven", "Pipeline Architecture", 
        "API Gateway", "Arquitectura sin Servidor", "Funcional Reactiva", 
        "Arquitectura híbrida", "BFF (Backend for Frontend)"
    ],
    "Año de Tendencia": [
        2023, 2020, 2023, 2022, 2021, 2023, 2022, 2023, 
        2022, 2023, 2023, 2021, 2022, 2023, 2021, 2022, 
        2023, 2023, 2021, 2022
    ],
    "Popularidad (%)": [
        94, 70, 88, 85, 82, 78, 83, 86, 79, 92, 91, 75, 
        80, 84, 78, 81, 89, 85, 74, 76
    ]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Configurar la gráfica
plt.figure(figsize=(12, 8))
plt.barh(df["Arquitectura"], df["Popularidad (%)"], color='skyblue')
plt.xlabel('Popularidad (%)')
plt.ylabel('Arquitectura')
plt.title('Popularidad de las Arquitecturas de Software en Diferentes Años')
plt.gca().invert_yaxis()  # Invertir el eje Y para que la barra más popular esté arriba
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.show()
