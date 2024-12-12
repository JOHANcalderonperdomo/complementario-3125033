import pandas as pd
import matplotlib.pyplot as plt

# Datos proporcionados
data = {
    "ID": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ],
    "Herramienta/Metodología": [
        "Kubernetes", "Docker", "Jenkins", "Ansible", "Terraform", 
        "CI/CD", "GitOps", "Prometheus", "Grafana", 
        "ELK Stack", "Helm", "Spinnaker", "Argo CD", 
        "CircleCI", "AWS CodePipeline", "Azure DevOps", 
        "Google Cloud Build", "Bamboo", "Chef", "SaltStack"
    ],
    "Año de Tendencia": [
        2023, 2023, 2022, 2023, 2023, 
        2022, 2023, 2022, 2023, 
        2022, 2023, 2023, 2023, 
        2021, 2023, 2022, 
        2023, 2021, 2021, None  # None porque falta el año para SaltStack
    ],
    "Popularidad (%)": [
        95, 93, 89, 85, 88, 
        92, 86, 84, 87, 
        83, 81, 80, 84, 
        79, 88, 82, 
        90, 75, 78, 0  # 0 porque falta el valor de popularidad para SaltStack
    ]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Filtrar filas con popularidad no nula
df = df[df["Popularidad (%)"] > 0]

# Configurar la gráfica de torta
plt.figure(figsize=(10, 10))
plt.pie(
    df["Popularidad (%)"], 
    labels=df["Herramienta/Metodología"], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=plt.cm.Paired.colors
)
plt.title('Popularidad de Herramientas y Metodologías')
plt.axis('equal')  # Asegurar que el gráfico de torta sea circular
plt.tight_layout()  # Ajustar diseño para mejor presentación
plt.show()
