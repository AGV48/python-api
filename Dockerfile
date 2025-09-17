# Imagen base de Python que utiliza la versión 3.7.11
FROM python:3.7.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR  /python-api

# Copia el archivo de requisitos al contenedor
COPY requirements.txt requirements.txt

# Instala las dependencias listadas en requirements.txt
RUN pip install -r requirements.txt

# Copia todo el contenido del proyecto al contenedor
COPY . .

# Ejecuta la aplicación Flask cuando el contenedor se inicie
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
