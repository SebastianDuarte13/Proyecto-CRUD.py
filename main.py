import streamlit as st
import sqlite3
import pandas as pd
import json
from datetime import datetime


st.set_page_config(page_title="Gestión de Tareas", layout="wide")

# Función para crear la tabla de tareas si no existe
def crear_tabla():
    conn = sqlite3.connect('tareas.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tareas
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         titulo TEXT NOT NULL,
         descripcion TEXT,
         completada INTEGER DEFAULT 0)
    ''')
    conn.commit()
    conn.close()

# Función para agregar una tarea
def agregar_tarea(titulo, descripcion):
    conn = sqlite3.connect('tareas.db')
    c = conn.cursor()
    c.execute("INSERT INTO tareas (titulo, descripcion) VALUES (?, ?)", (titulo, descripcion))
    conn.commit()
    conn.close()

# Función para obtener todas las tareas
def obtener_tareas():
    conn = sqlite3.connect('tareas.db')
    tareas = pd.read_sql_query("SELECT * FROM tareas", conn)
    conn.close()
    return tareas

# Función para marcar una tarea como completada
def marcar_completada(id):
    conn = sqlite3.connect('tareas.db')
    c = conn.cursor()
    c.execute("UPDATE tareas SET completada = 1 WHERE id = ?", (id,))
    conn.commit()
    conn.close()

# Función para eliminar una tarea
def eliminar_tarea(id):
    conn = sqlite3.connect('tareas.db')
    c = conn.cursor()
    c.execute("DELETE FROM tareas WHERE id = ?", (id,))
    conn.commit()
    conn.close()

# Función para exportar tareas
def exportar_tareas():
    tareas = obtener_tareas()
    return tareas.to_json(orient='records')

# Función para importar tareas
def importar_tareas(tareas_json):
    tareas = pd.read_json(tareas_json)
    conn = sqlite3.connect('tareas.db')
    tareas.to_sql('tareas', conn, if_exists='replace', index=False)
    conn.close()


crear_tabla()


st.title("Lista de Tareas")

# Sección para agregar tareas
st.header("Agregar Tarea")
col1, col2 = st.columns(2)
with col1:
    titulo = st.text_input("Título de la tarea")
with col2:
    descripcion = st.text_input("Descripción de la tarea")
if st.button("Agregar Tarea"):
    if titulo:
        agregar_tarea(titulo, descripcion)
        st.success("Tarea agregada con éxito!")
        st.rerun() 
        st.error("Por favor, ingrese un título para la tarea.")

# Sección para listar tareas
tareas = obtener_tareas()
for _, tarea in tareas.iterrows():
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.write(f"**{tarea['titulo']}** - {tarea['descripcion']}")
    with col2:
        if not tarea['completada']:
            if st.button("Marcar Completada", key=f"comp_{tarea['id']}"):
                marcar_completada(tarea['id'])
                st.rerun()  
            st.write("Completada")
    with col3:
        if st.button("Eliminar", key=f"del_{tarea['id']}"):
            eliminar_tarea(tarea['id'])
            st.rerun()  

# Sección para exportar e importar tareas
st.header("Exportar/Importar Tareas")
col1, col2 = st.columns(2)
with col1:
    if st.button("Exportar Tareas"):
        tareas_json = exportar_tareas()
        st.download_button(
            label="Descargar Tareas",
            data=tareas_json,
            file_name=f"tareas_exportadas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )
with col2:
    tareas_file = st.file_uploader("Seleccionar archivo de tareas para importar", type=['json'])
    if tareas_file is not None:
        if st.button("Importar Tareas"):
            tareas_json = tareas_file.getvalue().decode('utf-8')
            try:
                importar_tareas(tareas_json)
                st.success("Tareas importadas con éxito!")
                st.rerun() 
            except Exception as e:
                st.error(f"Error al importar tareas: {str(e)}")