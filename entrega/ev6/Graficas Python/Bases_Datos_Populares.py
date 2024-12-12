import pandas as pd
import matplotlib.pyplot as plt

# Datos proporcionados
data = {
    "ID": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ],
    "Base de Datos": [
        "MySQL", "PostgreSQL", "MongoDB", "SQLite", "Firebase", 
        "Cassandra", "Redis", "Oracle", "SQL Server", "DynamoDB", 
        "Elasticsearch", "MariaDB", "Couchbase", "Neo4j", "ArangoDB", 
        "Apache HBase", "CockroachDB", "InfluxDB", "CouchDB", "GraphQL"
    ],
    "Año de Tendencia": [
        2023, 2023, 2022, 2023, 2023, 
        2022, 2023, 2021, 2022, 2023, 
        2023, 2021, 2022, 2023, 2022, 
        2021, 2023, 2022, 2020, 2023
    ],
    "Popularidad (%)": [
        95, 92, 90, 88, 85, 80, 87, 79, 
        82, 84, 86, 78, 75, 83, 77, 71, 
        79, 74, 68, 88
    ]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Configurar la gráfica lineal
plt.figure(figsize=(12, 6))
plt.plot(df["Base de Datos"], df["Popularidad (%)"], marker='o', linestyle='-', color='b')
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor legibilidad
plt.xlabel('Base de Datos')
plt.ylabel('Popularidad (%)')
plt.title('Popularidad de las Bases de Datos en Diferentes Años')
plt.grid(True)
plt.tight_layout()  # Ajustar diseño para evitar superposición de etiquetas
plt.show()
