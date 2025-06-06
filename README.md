# 📊 Proyectos colaborativos  Sprint 7


## 🎯 Proyecto colaborativo: Dashboard con Streamlit

Este proyecto tiene como objetivo que los estudiantes trabajen en equipo para construir y desplegar una aplicación web interactiva utilizando **Streamlit**, a partir del análisis exploratorio de un conjunto de datos. Cada equipo podrá elegir entre tres datasets disponibles: uso de bicicletas, juegos de Steam o películas de IMDB.  

Deberán:
* Clonar el repositorio base.
* Realizar el EDA inicial en Jupyter Notebook.
* Crear una aplicación con al menos un filtro y una visualización interactiva.
* Confirmar los cambios en GitHub. (pueden crear una rama local o subirlo algún repositorio propio)

El trabajo se evaluará por la correcta estructura del proyecto, la funcionalidad del dashboard y la colaboración en equipo. 🚀

El repo incluye un ejemplo que puedes usar de referencia:

```bash

streamlit run movie_app.py

```

![Ejemplo en render](https://sp7-colaborative-project.onrender.com/)



### 📌 Notas importantes:

* El nombre del CSV puede variar (`bikes.csv`, `steam_games.csv`, `imdb_movies.csv`), pero debe estar en la raíz del proyecto.
* El archivo `requirements.txt` debe contener al menos:
  ```
  pandas
  plotly-express
  streamlit
  ```
* El archivo `EDA.ipynb` debe contener gráficos y primeras impresiones sobre los datos.
* `README.md` debe incluir:
  - Descripción del dataset
  - Instrucciones para ejecutar la app
  - URL del despliegue (una vez publicado en Render)

### Adicion de una nueva WebApp

Esta nueva aplicacion contiene el analicis de Rentas de Bicicletas en general, podran encontrar un barra de seleccion en la que podras elegir entre 2 tipos de Graficas `Barras` e `Histogramas` asi como tambien un boton ubicado debajop de la grafica principal que te permitira generar una grafica de `Disperción`.

---

## 🐍 Ejercicio: Tu primera calculadora desde consola

En este ejercicio trabajarás con clases en Python y el módulo `argparse` para construir una calculadora simple que puedas usar desde la terminal.

A partir del siguiente código base, deberás completar los métodos faltantes e implementar la lógica que permita ejecutar diferentes operaciones desde línea de comandos.

### Objetivos

1. Agregar los siguientes métodos a la clase `Calculator`:
   * `subtract(a, b)`
   * `multiply(a, b)`
   * `divide(a, b)` → **Manejo especial si `b == 0`**

2. Completar la lógica dentro del método `operate()` para que se ejecuten correctamente las nuevas operaciones según el argumento `--operation`.

3. (Opcional) Crear un nuevo método llamado `show_memory()` que imprima el último resultado guardado en el atributo `memory`.

---

### Ejemplos de uso esperado

```bash
# Suma simple
python calculator.py --operation add --numbers 5 3
```

> 8.0

```bash
# Multiplicación en modo verbose
python calculator.py --operation multiply --numbers 2 4 --verbose
```

> 🧮 Multiplying 2.0 * 4.0 = 8.0

```bash
# División por cero
python calculator.py --operation divide --numbers 10 0
```

> ❌ Error: No se puede dividir entre cero.

---

> ✅ ¡Usa `--verbose` para ver mensajes detallados!
> ✅ Recuerda que puedes usar `argparse` para recibir argumentos desde la línea de comandos.

