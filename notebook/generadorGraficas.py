import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dataFrameAsistencia = pd.read_csv("./data/asistencia_estudiantes_completo.csv")

#GRAFICANDO

# Grafica de barras
colors = ["#5ec29f", "#3fa99c", "#2d9093", "#2b7884", "#2e5f70", "#2f4858"]
plt.figure(figsize=(8, 5))
sns.countplot(data=dataFrameAsistencia, x='estado', palette=colors)
plt.title('Cantidad de Registros por Estado de Asistencia')
plt.xlabel("Estado de Asistencia")
plt.ylabel("Cantidad de Registros")
plt.tight_layout()
plt.show()

# Grafica de Torta
# Mostrar Proporciones entre dos columnas del DataFrame (Proporcion de estudiantes x Medio de Transporte)
conteoMedioTransporte = dataFrameAsistencia['medio_transporte'].value_counts()

plt.figure(figsize=(5, 5))
plt.pie(
    conteoMedioTransporte,
    labels=conteoMedioTransporte.index,
    autopct='%1.1f%%',
    colors = sns.color_palette("Blues")
)
plt.title("Distribución de Estudiantes por Medio de Transporte")
plt.tight_layout()
plt.show()

#Grafico de Barras Agrupadas
# Se aplica cuando hice cruces en el dataframe

#Converstir la matriz en una lista para poderla graficar

conteoEstadoMedioTransporte = dataFrameAsistencia.groupby(['estado', 'medio_transporte']).size().unstack(fill_value=0)

conteoEstadoMedioTransporte.plot(
    kind='bar',
    figsize=(10, 6),
    color = colors
)
plt.title('Registros por Estado de Asistencia y Medio de Transporte')
plt.xlabel("Estado de Asistencia")
plt.ylabel("Cantidad de Registros")
plt.legend(title='Medio de Transporte')
plt.tight_layout()
plt.show()

# Nueva gráfica 1: Histograma de registros por fecha
plt.figure(figsize=(10, 5))
dataFrameAsistencia['fecha'] = pd.to_datetime(dataFrameAsistencia['fecha'])
sns.histplot(data=dataFrameAsistencia, x='fecha', bins=15, color='#3fa99c')
plt.title('Cantidad de Registros por Fecha')
plt.xlabel('Fecha')
plt.ylabel('Cantidad de Registros')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Nueva gráfica 2: Gráfico de barras por estrato socioeconómico
plt.figure(figsize=(7, 5))
sns.countplot(data=dataFrameAsistencia, x='estrato', palette='viridis')
plt.title('Cantidad de Registros por Estrato Socioeconómico')
plt.xlabel('Estrato')
plt.ylabel('Cantidad de Registros')
plt.tight_layout()
plt.show()