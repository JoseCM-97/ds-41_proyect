import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(page_title="Visualización de Datos", page_icon="📊", layout="wide")

# Título de la aplicación
st.title("📊 Análisis de Datos de Bicicletas")

# Cargar dataset
df = pd.read_csv('./dataset/bikes.csv') 

# Sidebar para la selección
st.sidebar.header("Opciones de Gráficos")
chart_type = st.sidebar.selectbox("Selecciona el tipo de gráfico", ["Barras", "Histograma"])

def map_season(season_id):
    seasons={
        1:'Invierno',
        2: 'Primavera',
        3: 'Verano',
        4:'Otoño'
    }
    return seasons.get(season_id,'Desconocido')

metric=(
    df
        .groupby('season',as_index=False)
        .agg(n_dias =('cnt','sum'))
        
)
metric['season'] = metric['season'].apply(map_season)

metric.sort_values(by='n_dias',ascending=False)

if chart_type == "Barras":
    fig = px.bar(
    metric,
    x='season',
    y='n_dias',
    color='season',
    color_discrete_sequence=['blue', 'green', 'orange', 'red'],
    labels={'season': 'Estación', 'n_dias': 'Total de rentas'},
    title='Total de rentas por estación'
    )
    fig.update_layout(showlegend=False)
    fig.show()
else:
    season_labels = {
    1: 'Invierno',
    2: 'Primavera',
    3: 'Verano',
    4: 'Otoño'
    }


    df['season_name'] = df['season'].map(season_labels)

    # Crear histograma con plotly express
    fig = px.histogram(
        df,
        x='cnt',
        color='season_name',
        nbins=30,
        barmode='overlay',  # para que se superpongan
        opacity=0.6,         # transparencia para ver la superposición
        labels={'cnt': 'Cantidad de rentas', 'season_name': 'Estación'},
        title='Distribución de rentas por hora según estación'
    )

    fig.show()

# Mostrar gráfico en Streamlit
st.plotly_chart(fig, use_container_width=True)
season_labels = {
    1: 'Invierno',
    2: 'Primavera',
    3: 'Verano',
    4: 'Otoño'
    }


df['season_name'] = df['season'].map(season_labels)

hist_button = st.button('Construir scatter') # crear un botón  
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.header('Gráfica de dispersión: cantidad de rentas vs temperatura')
    st.write('Creación de una Grafica de Dispersion')   
    # crear un histograma

    fig = px.scatter(
    df,
    x='temp',
    y='cnt',
    color='season_name',
    labels={'temp': 'Temperatura Normalizada', 'cnt': 'Cantidad de rentas', 'season_name': 'Estación'},
    title='Dispersión de cantidad de rentas vs temperatura por estación',
    opacity=0.7
    )
    fig.show()

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)