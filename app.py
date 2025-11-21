import streamlit as st

st.set_page_config(page_title="Timeline", layout="centered")

st.title("Timeline con Slider e Imágenes desde GitHub")

# --- URL base del repositorio ---
BASE_URL = "https://github.com/danielgarcp-ux/Timeline_S1/new/main/timeline_images/"

# Lista de nombres de imágenes (asegúrate que coincidan con los nombres exactos en GitHub)
images = [
    "img1.jpg",
    "img2.jpg",
    "img3.jpg",
]

# Slider con posiciones del 1 al 3
pos = st.slider("Selecciona un punto del timeline", 1, 3, 1)

# Mostrar imagen correspondiente
img_url = BASE_URL + images[pos - 1]
st.image(img_url, use_column_width=True)

st.write(f"Imagen mostrada: {images[pos - 1]}")
