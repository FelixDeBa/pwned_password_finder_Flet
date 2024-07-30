# Buscador de contraseñas en Brechas publicas en HIBP, desarrollada en Flet
Aplicacion desarrollada en flet para revisar si una contraseña ha sido encontrada en una brecha publica registrada en haveibeenpwned

La intencion de esta aplicacion desarrollada en flet es posteriormente exportarla a android, por lo que para ejecutarla de la forma en la que esta pensada es necesario descargar la aplicacion Flet de la Google Play Store, posteriormente ejecutar la aplicacion con: 

flet run --android

Esto mostrara un codigo QR, el cual al escanearlo con la camara del celular y abrir el link resultante desde la aplicacion descargada Flet para Android te permitira testear la aplicacion

Para ejecutar desde la web, ejecutar

flet run --web

Para ejecutarlo como una aplicacion nativa de windows, linux o MacOS (No estoy muy seguro de macOS), ejecutar

flet run main.py

Este programa depende de las librerias requests y flet
Para instalarlas desde windows ejecutar:

pip install flet

Requests por lo general esta instalada por defecto, pero para instalarla es necesario

pip install requests

Para instalarlas en un Linux es necesario crear primero un entorno virtual con la libreria venv, para esto las instrucciones de Debian son las siguientes
sudo apt install python3-venv
python3 -m venv flet
source flet/bin/activate

Despues de estos 3 pases aparecera el nombre del entorno virtual entre parentesis (flet) al inicio de la carpeta en la que nos encontramos

Crear el entorno virutal es casi forzoso en linux, pero para propositos de desarrollo es recomendable hacerlo tanto en windows como en Linux

Una vez creado el entorno virutal se pued einstalar flet con 
pip install flet
y requests con 
pip install requests

