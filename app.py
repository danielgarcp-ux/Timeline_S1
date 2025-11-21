import streamlit as st

st.title("Timeline con Slider – Imágenes desde GitHub")

# URL base de las imágenes en GitHub
BASE_URL = "https://raw.githubusercontent.com/danielgarcp-ux/Timeline_S1/main/timeline_images/"

# Nombres exactos de las imágenes
imagenes = [
    "img1.png",
    "img2.png",
    "img3.png"
]

# Construye URLs completas
img_urls = [BASE_URL + img for img in imagenes]

# Slider con 3 posiciones
pos = st.slider(
    "Selecciona un punto de la línea de tiempo",
    min_value=0,
    max_value=2,
    value=0,
    step=1
)

# Mostrar imagen correspondiente
st.image(img_urls[pos], use_column_width=True)
