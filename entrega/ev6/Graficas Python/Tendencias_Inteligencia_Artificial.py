import pandas as pd
import matplotlib.pyplot as plt

# Datos proporcionados
data = {
    "ID": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ],
    "Tecnología IA": [
        "Procesamiento de Lenguaje Natural (NLP)", "Aprendizaje Profundo (Deep Learning)", 
        "Redes Neuronales Generativas (GANs)", "IA Conversacional (Chatbots)", 
        "Machine Learning Tradicional", "Visión Artificial (Computer Vision)", 
        "Modelos de IA Explicables", "IA en Seguridad Cibernética", 
        "Detección de Fraudes con IA", "Vehículos Autónomos", 
        "Sistemas Recomendadores", "IA en Salud (Diagnósticos)", 
        "Asistentes Virtuales", "Modelos de Lenguaje (GPT, BERT)", 
        "Robótica Autónoma", "Análisis Predictivo", 
        "IA en Agricultura (Drones, Sensores)", "IA en Finanzas", 
        "IA en Automatización de Procesos", "Sistemas de IA Personalizados"
    ],
    "Año de Tendencia": [
        2023, 2023, 2022, 2023, 2021, 2023, 
        2022, 2023, 2023, 2022, 
        2023, 2023, 2021, 2023, 
        2022, 2021, 2023, 2022, 
        2023, 2023
    ],
    "Popularidad (%)": [
        92, 95, 88, 89, 85, 93, 
        84, 91, 87, 90, 
        92, 89, 83, 96, 
        88, 82, 80, 85, 
        87, 84
    ]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Configurar la gráfica de torta
plt.figure(figsize=(12, 12))
plt.pie(
    df["Popularidad (%)"], 
    labels=df["Tecnología IA"], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=plt.cm.Paired.colors, 
    wedgeprops={'edgecolor': 'black'}  # Añadir borde negro a cada segmento
)
plt.title('Popularidad de Tecnologías de IA')
plt.axis('equal')  # Asegurar que el gráfico de torta sea circular
plt.tight_layout()  # Ajustar diseño para mejor presentación
plt.show()
