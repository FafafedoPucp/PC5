##Libreria
import streamlit as st

#Cambiar el color del fondo
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


st.image('fotoperfil.JPG', width=200)

##Título
st.title("Erick Farfan de la Cruz")

### Subtítulo
st.subheader("Sobre mi")

# Párrafo
st.write("¡Hola! Actualmente soy estudiante de Comunicación Audiovisual en la Pontificia Universidad Católica del Perú (5to ciclo) y me encanta programar en Python")
st.write("Soy un líder seguro que encuentra soluciones creativas y sencillas, mantiene buenas relaciones interpersonales con un carácter amigable y emprendedor, promoviendo tolerancia, amabilidad, justicia y equidad.")

## Educación
st.subheader("Educación")
### Pontificia Universidad Católica del Perú

st.write("**Comunicación audiovisual**")
st.write("mar. 2023 - dic. 2027")
st.write("Aptitudes: Cine, Guion y Fotografía")

st.write("---") #Separador
### Colegio Salesiano San Juan Bosco de Ayacucho
st.write("**Educación Secundaria Obligatoria (ESO)**")
st.write("mar. 2011 - dic. 2022")
st.write("Actividades y grupos: Cantante, comunicador, regidor de tecnología y comunicación y sub-brigadier general")
st.write("Aptitudes: Fotografía y Publicidad")

## Experiencia 
st.subheader("Experiencia")

### Asistente de cámara
st.write("**Llipiq Producciones · Jornada completa**")
# Usamos la clase small-text para las fechas y duración
st.markdown('<p class="small-text">dic. 2023 - mar. 2024 · 4 meses</p>', unsafe_allow_html=True)
st.write("Provincia de Huamanga, Departamento de Ayacucho, Perú · Presencial")

## Portafolio Fotográfico
st.title("Portafolio")
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

## Conexión

st.write("Puedes encontrarme en mis redes sociales y contactarme por correo:")
st.write("---") # Una línea divisoria para separar el contenido principal

st.write("[LinkedIn](https://www.linkedin.com/in/efarfa118/) | [Instagram](https://www.instagram.com/e.farfa11) | [Correo](mailto:efarfan118@gmail.com)")