# Introducción y Presentación de la Hipótesis
> El objetivo de este análisis es investigar si existe una correlación entre el año en el que un lenguaje de programación es tendencia y su nivel de popularidad. Mi hipótesis es que, a medida que los lenguajes se vuelven más relevantes en años recientes, tienen una mayor popularidad, reflejando las preferencias y tendencias del mercado.

## Explicación del Código

### Lectura y Preparación de los Datos
> Primero, leí los datos de un archivo CSV utilizando `pandas`, que me permite manejar la información en forma de una tabla. Después, seleccioné las columnas necesarias: `Año de Tendencia` y `Popularidad (%)`, asegurándome de que estuvieran listas para análisis.

### Análisis de Correlación
> Usé la biblioteca `scipy.stats` para calcular la correlación entre estas dos variables. La función `linregress` me permitió obtener el coeficiente de correlación `r`, que indica la fuerza y dirección de la relación entre las variables.

### Creación de la Gráfica
> Para representar visualmente esta relación, utilicé `matplotlib` y `seaborn`. En la gráfica de dispersión, cada punto representa un lenguaje con su año de tendencia en el eje X y su popularidad en el eje Y. Además, añadí una línea de tendencia basada en el análisis de regresión para mostrar la dirección general de la correlación.

## Explicación de la Gráfica

### Elementos Visuales
> Aquí, cada punto azul representa un lenguaje de programación. En el eje X tenemos el año en el que el lenguaje fue tendencia, y en el eje Y está su popularidad medida en porcentaje.

### Línea de Tendencia
> La línea roja representa la tendencia general entre las variables. Su pendiente positiva indica que, en general, los lenguajes más recientes tienden a tener mayores niveles de popularidad.

### Interpretación del Coeficiente de Correlación
> El valor de `r`, que es 0.70, sugiere una correlación positiva moderada. Esto significa que existe una tendencia a que los lenguajes recientes sean más populares, pero no es una regla estricta.

## Conclusión
> Basándonos en esta gráfica y el análisis, podemos observar que los lenguajes que han sido tendencia en años más recientes tienden a ser más populares, lo que confirma parcialmente nuestra hipótesis. Sin embargo, algunos lenguajes, como Ruby o Perl, no siguen esta tendencia, lo que indica que otros factores también influyen en la popularidad de los lenguajes.
