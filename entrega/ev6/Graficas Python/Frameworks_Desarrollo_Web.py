import pandas as pd
import matplotlib.pyplot as plt

# Datos proporcionados
data = {
    "ID": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ],
    "Framework": [
        "React", "Angular", "Vue.js", "Svelte", "Next.js", 
        "Nuxt.js", "Django", "Flask", "Ruby on Rails", "Laravel", 
        "Express.js", "Spring", "ASP.NET", "Meteor", "Backbone.js", 
        "Ember.js", "FastAPI", "Phoenix", "Strapi", "Blazor"
    ],
    "Año de Tendencia": [
        2023, 2022, 2023, 2023, 2023, 
        2022, 2023, 2021, 2020, 2023, 
        2022, 2022, 2021, 2020, 2021, 
        2020, 2023, 2022, 2023, 2022
    ],
    "Popularidad (%)": [
        95, 85, 90, 82, 88, 84, 87, 80, 
        75, 86, 83, 81, 78, 74, 70, 68, 
        88, 80, 82, 76
    ]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Configurar la gráfica lineal
plt.figure(figsize=(12, 6))
plt.plot(df["Framework"], df["Popularidad (%)"], marker='o', linestyle='-', color='blue')
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor legibilidad
plt.xlabel('Framework')
plt.ylabel('Popularidad (%)')
plt.title('Popularidad de los Frameworks en Diferentes Años')
plt.grid(True)
plt.tight_layout()  # Ajustar diseño para evitar superposición de etiquetas
plt.show()
