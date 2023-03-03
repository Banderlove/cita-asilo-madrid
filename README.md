Este script de selenium te ayuda a coger cita para asilo en CNP/ExtranjeriaMadrid

Activa el volumen para escuchar el pítido fuerte que emite el programa cuando encuentra cita/citas disponibles.

Trámites disponibles:
-------------
- POLICIA - SOLICITUD ASILO

Provincia:
- Madrid

Instalación
-------------------

1. Descarga e instala [Python](https://www.python.org/downloads/).

2. Abre cmd en la carpeta donde tengas este proyecto y escribe `pip install -r requirements.txt`

3. Instala Google Chrome.

4. Descargar [chromedriver](https://chromedriver.chromium.org/downloads) y ponlo en el directorio raíz de Python.

6. Edita el archivo `cita-asilo.py` con un bloc de notas o un editor de código e introduce tus datos personales:
   
   Línea 113 sustituye "PASSPORT" por tu número de pasaporte,tiene que llevar comillas "",ejemplo: "185201478".
   
   Línea 123 sustituye" "NAME LASTNAME LASTNAME" por tu nombre y apellidos que aparezcan en tu pasaporte,tiene que llevar "",ejemplo: "ALBERTO TORRES RUIZ".
   
   Línea 130 sustituye "YEAR" por tu fecha de nacimiento que aparezca en tu pasaporte,tiene que llevar comillas "",ejemplo: "1986".
   
   Línea 140 sustituye el valor "248" por el país de tu nacionalidad: revisa el archivo [nacionalidades.txt](https://github.com/MisterDarkZ/cita-asilo-madrid/blob/main/nacionalidades.txt) y sustituye el valor 248 por el código de tu país.
   
7. Abre cmd y escribe `cita-asilo.txt python3`.

CUANDO EL BOT ENCUENTRA CITA EMITE UN PITIDO CONSTANTE,POR LO QUE ACTIVA Y SUBE EL VOLUMEN DE ORDENADOR PARA PODER ESCUCHARLO,CUANDO ENCUENTRA CITA TIENES 10 MINUTOS PARA RELLENAR TUS DATOS MANUALMENTE PORQUE SI NO EN 10 MINUTOS SE CIERRA EL NAVEGADOR Y EL BOT.

EL BOT SIEMPRE VA A ESTAR FUNCIONANDO HASTA QUE ENCUENTRE UNA CITA DISPONIBLE SIEMPRE Y CUANDO LA PÁGINA DE CITAS ESTÉ FUNCIONANDO Y NO SE CAIGA,SI SALE ERROR DE MUCHOS INTENTOS DEBES DE APAGAR EL NAVEGADOR QUE ABRIÓ SELENIUM,CERRAR CMD,ESPERAR UNOS 2-3 MINUTOS Y VOLVER A ENCENDER EL BOT.
