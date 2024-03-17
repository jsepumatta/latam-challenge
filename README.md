# LATAM CHALLENGE

Este proyecto Python proporciona una serie de funciones para analizar datos de Twitter y encontrar usuarios influyentes basados en menciones, contar la frecuencia de emojis en los tweets y determinar las fechas más activas en términos de cantidad de tweets. A continuación, se proporciona una descripción detallada de cada función y cómo instalar las dependencias necesarias para ejecutar el código.

## Funciones proporcionadas:

### q1_time
Esta función procesa un archivo JSON de tweets y determina las fechas más activas y los usuarios más activos en esas fechas.

### q1_memory
Esta función optimiza el uso de memoria al procesar un archivo JSON de tweets para determinar las fechas más activas y los usuarios más activos en esas fechas.

### q2_time
Esta función cuenta la frecuencia de emojis en los tweets presentes en un archivo JSON.

### q2_memory
Esta función optimiza el uso de memoria al contar la frecuencia de emojis en los tweets presentes en un archivo JSON.

### q3_time
Esta función analiza un archivo de texto para encontrar los usuarios más influyentes basados en menciones.

### q3_memory
Esta función optimiza el uso de memoria al analizar un archivo de texto para encontrar los usuarios más influyentes basados en menciones.

## Instalación de dependencias:

Para ejecutar este proyecto, primero debe instalar las dependencias necesarias. Puede hacerlo ejecutando el siguiente comando en su terminal:

```sh 
pip install -r requirements.txt
```

Este comando instalará todas las dependencias especificadas en el archivo `requirements.txt`.

## Uso del proyecto:

Una vez instaladas las dependencias, puede ejecutar cada función proporcionada ejecutando el script correspondiente desde la línea de comandos o en un entorno de desarrollo Python.

Por ejemplo, para ejecutar la función `q1_time`, puede usar el siguiente comando:

```sh 
python q1_time.py farmers-protest-tweets-2021-2-4.json
```

Reemplace `farmers-protest-tweets-2021-2-4.json` con la ruta de su propio archivo JSON de tweets.

## Notas adicionales:

- Asegúrese de tener los permisos adecuados para acceder al archivo JSON y al archivo de texto, dependiendo de su sistema operativo.
- Siempre es recomendable ejecutar el código en un entorno virtual de Python para evitar conflictos de dependencias con otros proyectos.
