import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Cargar el dataset
df = pd.read_csv("dataset/imdb_movies.csv")

# Convertir la columna 'Gross' a numérica (limpieza mínima)
df['Gross'] = pd.to_numeric(df['Gross'].str.replace(',', ''), errors='coerce')

# Título de la app
st.title("🎬 Dashboard de Películas IMDB")

# Sección 1: Vista previa de la tabla
st.subheader("👀 Vista previa del dataset")
st.dataframe(df.head())

# Sección 2: Gráfico interactivo
st.subheader("📊 Análisis de recaudación por clasificación")

# Selector de gráfico
use_plotly = st.checkbox("Usar gráfico Plotly", value=True)

if use_plotly:
    fig = px.box(df, x="Certificate", y="Gross", title='Distribución de "Gross" por clasificación')
    st.plotly_chart(fig)
else:
    st.write("Gráfico generado con Matplotlib:")
    fig, ax = plt.subplots()
    df.boxplot(column='Gross', by='Certificate', ax=ax)
    ax.set_title('Distribución de "Gross" por clasificación')
    ax.set_xlabel('Clasificación')
    ax.set_ylabel('Recaudación (Gross)')
    plt.suptitle("")
    st.pyplot(fig)
