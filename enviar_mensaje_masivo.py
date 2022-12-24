"INSTALA LA LIBRERIA pip install pywhatkit "

import pywhatkit

# Iniciar el servidor
# pywhatkit.start_server()

# Crear una lista de números de teléfono
numeros = ['+52 1 55 1186 9158']

# Enviar mensaje a cada número de teléfono
for numero in numeros:
    pywhatkit.sendwhatmsg_instantly(numero, """Holaaaaaaaaa. ¡Feliz Navidad! Espero que estés pasando unas fiestas maravillosas rodeado de tu familia y amigos.

    Quiero aprovechar esta ocasión para expresar mis mejores deseos hacia ti y para desearte un año lleno de éxitos y felicidad. Espero que puedas disfrutar al máximo de estas fiestas y que puedas relajarte y descansar junto a tu familia.

    La Navidad es un tiempo para celebrar y reflexionar sobre lo que hemos logrado durante el año. Estoy seguro de que has tenido muchos triunfos y logros que celebrar, y espero que puedas seguir trabajando duro y alcanzando tus metas en el año que viene.

    Ojalá puedas disfrutar de esta época del año con los tuyos y puedas compartir momentos especiales y alegres con ellos. Que tengas una maravillosa Navidad y un próspero Año Nuevo. ¡Te deseo todo lo mejor!""")

