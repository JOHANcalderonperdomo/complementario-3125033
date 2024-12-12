import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# 1. Cargar los datos desde el archivo CSV
# Asegúrate de guardar el archivo como "datos.csv" en el mismo directorio que este script
df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Documentos\Char\Sena\Investigacion\Markdown\Correlacion\datos.csv", delimiter="\t")


# Verificar si los nombres de las columnas están correctos
df.columns = df.columns.str.strip()  # Eliminar espacios adicionales en los encabezados

# 2. Crear el diagrama de dispersión
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Ano de Tendenci', y='Popularidad (%)', data=df, color='blue', s=100)

# 3. Calcular la línea de regresión
slope, intercept, r_value, p_value, std_err = linregress(df['Ano de Tendenci'], df['Popularidad (%)'])
line = slope * df['Ano de Tendenci'] + intercept
plt.plot(df['Ano de Tendenci'], line, color='red', label=f'Línea de tendencia (r={r_value:.2f})')

# 4. Personalizar el gráfico
plt.title('Correlación entre Año de Tendencia y Popularidad (%)', fontsize=14)
plt.xlabel('Año de Tendencia', fontsize=12)
plt.ylabel('Popularidad (%)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# 5. Mostrar el gráfico
plt.show()
