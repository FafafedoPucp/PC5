##Libreria
import streamlit as st
from PIL import Image

st.markdown(
    """
    <style>
    .stApp {
        background-color: #002124;
    }
    </style>
    """,
    unsafe_allow_html=True
)

imagen_erick = Image.open('fotoperfil.jpg')
st.image(imagen_erick, caption='Foto de perfil', width=200)

##Título
st.title("Erick Farfan de la Cruz")

### Subtítulo
st.subheader("Sobre mi")

# Párrafo
st.write("¡Hola! Soy Erick Farfan de la Cruz. Me apasiona la comunicación audiovisual y la programación.")
st.write("Este es un segundo párrafo para mostrarte cómo agregar más texto.")

## Portafolio Fotográfico

### Subtítulo
st.subheader("Fotografías de Paisaje")
### Fotografía de Retrato
col1, col2, col3 = st.columns(3)
with col1:
    st.image("IMG_6425.jpg", width=200)
with col2:
    st.image("IMG_8625.jpg", width=200)
with col3:
    st.image("IMG_8840.jpg", width=200)
with col1:
    st.image("IMG_8891.jpg", width=200)
with col2:
    st.image("IMG_8973.jpg", width=200)
with col3:
    st.image("IMG_9086.jpg", width=200)
with col1:
    st.image("IMG_8736.jpg", width=200)
with col2:
    st.image("IMG_8735.jpg", width=200)
with col3:
    st.image("IMG_8656.jpg", width=200)
with col1:
    st.image("IMG_8622.jpg", width=200)


### Subtítulo
st.subheader("Fotografías de Retrato")
### Fotografía de Retrato
col1, col2, col3 = st.columns(3)
with col1:
    st.image("IMG_9964.jpg", width=200)
with col2:
    st.image("IMG_9945.jpg", width=200)
with col3:
    st.image("Paolo Guitarra Niña.jpg", width=200)

## Sección de Videos

st.subheader("Proyectos de video")
st.video("https://youtu.be/IVoQhfaI-LU?si=zPCW8QLpXhwFOEyf")

st.write("Este es un video sobre mi proyecto en conjunto con la banda Bacillus de Ayacucho en 2022. En este proyecto lo he producido en su totalidad yo con inversión de Rafael Arias")

## Conéctate Conmigo

st.write("Puedes encontrarme en mis redes sociales y contactarme por correo:")
st.write("---") # Una línea divisoria para separar el contenido principal

st.write("[LinkedIn](https://www.linkedin.com/in/efarfa118/) | [Instagram](https://www.instagram.com/e.farfa11) | [Correo](mailto:efarfan118@gmail.com)")