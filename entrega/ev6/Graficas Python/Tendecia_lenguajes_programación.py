import pandas as pd
import matplotlib.pyplot as plt

# Datos proporcionados
data = {
    "ID": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ],
    "Lenguaje": [
        "Python", "JavaScript", "Java", "C#", "Kotlin", 
        "Swift", "TypeScript", "PHP", "Rust", "Go", 
        "C++", "Ruby", "Dart", "Scala", "Elixir", 
        "R", "Perl", "Lua", "Haskell", "Julia"
    ],
    "Año de Tendencia": [
        2023, 2023, 2022, 2023, 2023, 
        2022, 2023, 2021, 2023, 2023, 
        2022, 2020, 2023, 2021, 2023, 
        2022, 2020, 2021, 2023, 2022
    ],
    "Popularidad (%)": [
        95, 94, 89, 87, 85, 83, 92, 77, 
        88, 84, 80, 75, 82, 78, 81, 76, 
        68, 72, 73, 79
    ]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Configurar la gráfica lineal
plt.figure(figsize=(12, 6))
plt.plot(df["Lenguaje"], df["Popularidad (%)"], marker='o', linestyle='-', color='blue')
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor legibilidad
plt.xlabel('Lenguaje')
plt.ylabel('Popularidad (%)')
plt.title('Popularidad de los Lenguajes de Programación en Diferentes Años')
plt.grid(True)
plt.tight_layout()  # Ajustar diseño para evitar superposición de etiquetas
plt.show()
