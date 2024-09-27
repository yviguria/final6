import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Formulario de Registro")

# Crear un DataFrame vacío o cargarlo desde un archivo
if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=[
        'Nombre Completo', 'Edad', 'Documento de Identidad', 
        'Dirección', 'Origen', 'Motivo de Consulta'
    ])

# Entradas del formulario
with st.form("Formulario"):
    nombre = st.text_input("Nombre Completo")
    edad = st.number_input("Edad", min_value=0, max_value=120, step=1)
    documento = st.text_input("Documento de Identidad")
    direccion = st.text_input("Dirección")
    origen = st.text_input("Origen (Región, Departamento, Distrito)")
    motivo = st.text_area("Motivo de Consulta")
    
    # Botón para enviar el formulario
    submitted = st.form_submit_button("Guardar Datos")
    
    # Guardar los datos en el DataFrame si se envía el formulario
    if submitted:
        nuevo_registro = {
            'Nombre Completo': nombre,
            'Edad': edad,
            'Documento de Identidad': documento,
            'Dirección': direccion,
            'Origen': origen,
            'Motivo de Consulta': motivo
        }
        st.session_state['data'] = st.session_state['data'].append(nuevo_registro, ignore_index=True)
        st.success("Datos guardados correctamente.")

# Mostrar los datos almacenados en el DataFrame
if st.button('Imprimir DataFrame'):
    st.write(st.session_state['data'])
