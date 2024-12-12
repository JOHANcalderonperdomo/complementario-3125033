import pandas as pd
import matplotlib.pyplot as plt

# Datos proporcionados
data = {
    "ID": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ],
    "Tecnología o Servicio Cloud": [
        "Computación en la Nube Pública", "Computación Híbrida", "Multicloud",
        "Contenedores (Docker, Kubernetes)", "Serverless Computing", "Almacenamiento en la Nube",
        "Seguridad en la Nube", "DevOps en la Nube", "Migración a la Nube",
        "Infraestructura como Código", "Servicios PaaS", "Servicios SaaS",
        "Edge Computing", "Gestión de Recursos Cloud", "Contenedores Desacoplados",
        "Cloud-Native Applications", "Alta Disponibilidad en la Nube", "Disaster Recovery en la Nube",
        "Machine Learning en la Nube", "Redes Definidas por Software (SDN)"
    ],
    "Año de Tendencia": [
        2023, 2023, 2023, 2023, 2023, 2023,
        2023, 2022, 2021, 2022, 2023, 2023,
        2023, 2022, 2023, 2022, 2023, 2022,
        2023, 2023
    ],
    "Popularidad (%)": [
        90, 87, 89, 93, 91, 88,
        85, 82, 80, 84, 86, 92,
        88, 83, 85, 81, 87, 78,
        89, 80
    ]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Configurar la gráfica de barras
plt.figure(figsize=(14, 8))
plt.barh(df["Tecnología o Servicio Cloud"], df["Popularidad (%)"], color='lightblue')
plt.xlabel('Popularidad (%)')
plt.ylabel('Tecnología o Servicio Cloud')
plt.title('Popularidad de Tecnologías y Servicios en la Nube')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.gca().invert_yaxis()  # Invertir el eje Y para que la barra más popular esté arriba
plt.tight_layout()  # Ajustar diseño para evitar superposición de etiquetas
plt.show()
