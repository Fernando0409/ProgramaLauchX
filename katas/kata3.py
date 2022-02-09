# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.

velocidadAsteroide = float(input("Velocidad del asteroide: "))
if velocidadAsteroide > 25:
    print("Un astereroide se acerca rapidamente a " +str(velocidadAsteroide)+ " km/s !!")
else:
    print("El asteroide tiene un comportamiento normal")

# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False
velocidadAsteroide = 19
if velocidadAsteroide > 20:
    print("Observa el cielo y pide un deseo!")
elif velocidadAsteroide == 20:
    print("Podras ver algo muy cool esta noche")
else:
    print("Ve a dormir de una vez")


# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.
sizeAsteroide = float(input("Tamaño del asteroide: "))
velocidadAsteroide = float(input("Velocidad del asteroide: "))

if sizeAsteroide > 25 and velocidadAsteroide > 25:
    print()
elif velocidadAsteroide >= 20:
    print("Saldran luces en el cielo!!")
elif sizeAsteroide < 25:
    print("Asteroide desintegrado!!")
else:
    print("Nada de que preocuparse")