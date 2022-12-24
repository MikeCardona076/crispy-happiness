"INSTALA LA LIBRERIA pip install pywhatkit "


import pywhatkit

pywhatkit.start_server()


lista_contactos = [

   '+5215511869158'
]


#Envia el Mensaje 

for i in lista_contactos:
    
    pywhatkit.sendwhatmsg_instantly(i, """Holaaaaaaaaa. ¡Feliz Navidad! Espero que estés pasando unas fiestas maravillosas rodeado de tu familia y amigos.

    Quiero aprovechar esta ocasión para expresar mis mejores deseos hacia ti y para desearte un año lleno de éxitos y felicidad. Espero que puedas disfrutar al máximo de estas fiestas y que puedas relajarte y descansar junto a tu familia.

    La Navidad es un tiempo para celebrar y reflexionar sobre lo que hemos logrado durante el año. Estoy seguro de que has tenido muchos triunfos y logros que celebrar, y espero que puedas seguir trabajando duro y alcanzando tus metas en el año que viene.

    Ojalá puedas disfrutar de esta época del año con los tuyos y puedas compartir momentos especiales y alegres con ellos. Que tengas una maravillosa Navidad y un próspero Año Nuevo. ¡Te deseo todo lo mejor!""", 4, False, 4)
