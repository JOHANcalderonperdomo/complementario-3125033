import pandas as pd
import matplotlib.pyplot as plt

# Datos proporcionados
data = {
    "ID": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ],
    "Tecnología de Seguridad": [
        "Autenticación Multifactor", "Zero Trust", "Cifrado Homomórfico", 
        "Seguridad en la Nube", "Identidad Digital", "Seguridad en IoT", 
        "Detección y Respuesta Extendida (XDR)", "Inteligencia Artificial en Seguridad", 
        "Blockchain para Seguridad", "Análisis de Seguridad Predictiva", 
        "Seguridad en DevOps (DevSecOps)", "Automatización de Seguridad", 
        "Seguridad en Contenedores", "Seguridad en Vehículos Autónomos", 
        "Cumplimiento de Normativas (GDPR, CCPA)", "Seguridad en Blockchain", 
        "Análisis Forense de Datos", "Gestión de Riesgos de Terceros", 
        "Modelos Zero-Knowledge", "Privacidad Computacional"
    ],
    "Año de Tendencia": [
        2023, 2023, 2022, 2023, 2023, 2023, 2022, 2023, 
        2022, 2023, 2023, 2023, 2023, 2023, 2021, 2022, 
        2023, 2022, 2023, 2023
    ],
    "Popularidad (%)": [
        90, 89, 83, 91, 87, 84, 85, 88, 
        80, 86, 87, 84, 83, 81, 82, 78, 
        80, 76, 79, 83
    ]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Configurar la gráfica de barras
plt.figure(figsize=(14, 8))
plt.barh(df["Tecnología de Seguridad"], df["Popularidad (%)"], color='skyblue')
plt.xlabel('Popularidad (%)')
plt.ylabel('Tecnología de Seguridad')
plt.title('Popularidad de Tecnologías de Seguridad en Diferentes Años')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.gca().invert_yaxis()  # Invertir el eje Y para que la barra más popular esté arriba
plt.tight_layout()  # Ajustar diseño para evitar superposición de etiquetas
plt.show()
