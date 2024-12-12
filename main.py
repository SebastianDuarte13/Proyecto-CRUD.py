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

