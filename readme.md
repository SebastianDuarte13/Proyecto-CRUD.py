# Gestor de Tareas

Este proyecto es una aplicación web de gestión de tareas construida con Streamlit y SQLite. Permite a los usuarios crear, visualizar, completar y eliminar tareas, así como exportar e importar listas de tareas.

## Características 🧑‍💻

- Agregar nuevas tareas con título y descripción
- Visualizar lista de tareas existentes
- Marcar tareas como completadas
- Eliminar tareas
- Exportar tareas a un archivo JSON
- Importar tareas desde un archivo JSON

## Requisitos 💫

- Python
- Streamlit
- Pandas
- SQLite3

## Instalación ♨️

1. Instale las dependencias necesarias:

## Usar un entorno virtual 🔧

Para evitar conflictos con otras instalaciones:

1. Crea un entorno virtual:

```cmd
python -m venv env
```

2. Actívalo:

```cmd
env\Scripts\activate
```

3. Instala Streamlit dentro del entorno:

```cmd
pip install streamlit
```

4. Ejecuta el script:

```cmd
streamlit run main.py
```

## Estructura del Código 💻

- El script comienza importando las bibliotecas necesarias y configurando la página de Streamlit.
- Se definen funciones para interactuar con la base de datos SQLite:
- `crear_tabla()`: Crea la tabla de tareas si no existe.
- `agregar_tarea()`: Agrega una nueva tarea a la base de datos.
- `obtener_tareas()`: Recupera todas las tareas de la base de datos.
- `marcar_completada()`: Marca una tarea como completada.
- `eliminar_tarea()`: Elimina una tarea de la base de datos.
- Se implementan funciones para exportar e importar tareas:
- `exportar_tareas()`: Convierte las tareas a formato JSON.
- `importar_tareas()`: Carga tareas desde un archivo JSON a la base de datos.
- La interfaz de usuario se construye usando componentes de Streamlit como `st.title()`, `st.header()`, `st.columns()`, etc.
- Se manejan las interacciones del usuario (agregar, completar, eliminar tareas) y se actualiza la interfaz en consecuencia.

## Notas 📃

- La aplicación usa `st.rerun()` para actualizar la interfaz después de cambios en las tareas.
- Los datos se almacenan localmente en un archivo SQLite llamado `tareas.db`.
- Las tareas exportadas se guardan en formato JSON con una marca de tiempo en el nombre del archivo.

## Contribuciones 🤝

Las contribuciones a este proyecto son bienvenidas. Por favor, deje su comentario y sugerencian en lo que podamos mejorar

cabe resaltar que nunca hania utilizado la libreria streamlit y todo fue gracias a distintos videos de youtube y documentación de la pagina de streamlit aqui la dejo por si gustan revisarla -> https://docs.streamlit.io/ 


## Requisitos del programa

![](/requisitos%20del%20programa.png)