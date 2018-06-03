
# Creación de un Software de Automatización de Tareas

Hola amigos de Mi Diario Python, les doy nuevamente las bienvenidas a nuestra bonita comunidad. Mi nombre es Luis ycomo siempre es un placer estar escribiendo esto para todos ustedes.

En el articulo de hoy, tocaremos un tema cuya importancia en el area de la programación es mucha. La Progrmaación  Orientada a Objetos.

Mi objetivo en este articulo es guiarlos y mostrarles los pasos para crear un pequeño software que nos permita automatizar funciones de n uestro ordenar. Con esto me refiero a que podremos realizar un script el cual pueda mover el mouse por si solo. Tambien crearemos funciones para el teclado. ¿Que te parece?.

Todos sabemos que existen muchas librerias que realizan estas funciones. Pero realizar el nuestro, nos ayudara a fortalecer nuestro conocimientos, y por supuesto, no hay nada más satisfactorio que utilizar nuestras propias herramnientas.

Antes de comenzar quisiera aclarar algunas cosas: Lo primero es que los pasos y funciones que realizaremos hoy estaran orientadas a usuario que utilizen Windows, esto se debe a que haremos uso de la libreria "win32", la cual nos permite interactuar con el sistema operativo. Otra cosa quiero aclarar, es que en este articulo no proundizare muchos en los detalles de la Programación Orientada a Objeto ni a principios basicos del Lenguaje Python ya que en este blog tenemos muy buenos articulos para Aprender Python, así que te sugiero que le heches un vistazo.

# Win32

Win32 es una libreria para Python que nos permite interactuar y manipular funciones de sistema operativo Windows. Tiene muchos metodos y funciones que debes conocer. Win32 tiene funciones para manipular archivos, conecciones de redes, seguridad del sistema y muchas otras más.

Puedes adquirir win32 ingresando al siguiente enlace: 

Win32 sera el unico recurso externo que utilizaremos el dia de hoy. Win32 tiene un modulo llamado "Win32api", el cual tiene una gran variedad de funciones y metodos, desde obtener la fecha local del equipo, hasta definir variables de entorno. Esta libreria nos permite conocer a fondo el equipo en el que se trabaja, incluyendo conocer la posición del cursor, definir su posición y saber el estado del teclado. Así que por esta razon la utilizaremos para realizar el proyecto de hoy.

# WindowsBot

WindowsBot sera el nombre del proyecto ¿Que les parece?.

Perfecto, ya podemos empezar con el proyecto. Lo primero que haremos sera abrir nuestro editor de texto preferido y crear un nuevo archivo. Yo trabajare de la siguiente manera: Creare una carpeta llamada WindowsBot y en ella creare un nuevo directorio llamado "winbot", en este directorio escribire los archivos de nuestro nuevo modulo. Así que yo trabajara en "WindowsBot/winbot", es aqui en donde escribiremos nuestras clases y metodos, luego podremos crear scripts de prueba que importen los arhcivos de este directorio.

No se si me explique bien, pero si tienes alguna duda sabes que puedes dejar tu comentario.

Mu bien, si tienen experiencia con lo de la Programación Orientada a Objetos sabran que si un modulo sin el arhcivo "__init__.py" no es un modulo. ¿Que es el archivo "__init__"? Este script, sera ejecutara cada vez que el modulo sea importado desde un script, así que pueden verlo como una función que se ejecutara cada vez que se use "import winbot" en un script de python.


```python
# winbot/__init__.py

print("Modulo importado exitosamente")
```

    Modulo importado exitosamente
    

Por ahora, dejaremos al arhcivo "__init__.py" con una simple función print, luego volveremos a este archivo.

Este arhcivo especial, nunca puede faltar en la creación de un modulo, podrias dejarlo vacio y todo iria bien, pero siempre debe de haber un arhcivo "__init__.py" en el lugar de trabajo.

prosigamos. Lo que haremos ahora sera crear el arhcivo "windows.py". En el escribiremos las clases y metodos que les permitiran manipular las funciones del cursor y el teclado del ordenador a cualquiera que importe este modulo:


```python
# winbot/windows.py

# Comencemos importanod las librerias necesarias
# Lo modulos win32 nos permitiran interactuar con el Sistema Operativo
import win32api
import win32con

class MouseBot():
    """
    Definimos la clase principal, en mi caso la he llamado MosueBot. En ella escribiremos los metodos
    para la manipulación del cursor.
    """
    
    
    """ 
    Definimos el metodo __init__ el cual tiene el mismo proposito que el archivo __init__.py.
    Es recomendable siempre definir este metodo, aunque este vacio.
    
    """
    def __init__(self):
        # __init__ se llamara la crearse una instancia de la clase MouseBot
        print("MouseBot se ha inicializado con exito")
        
    def getPosition(self):
        """
        El metodo getPosition retornara la posición actual del cursor.
        Para ello utilizaremos la función GetCursorPos de win32api.
        """
        pos = win32api.GetCursorPos()
        return pos

    
    def move(self, x, y):
        """
        El metodo move cambiara la posición del cursor con respecto asu eje x e y.
        """
        NewPos = [x, y]
        win32api.SetCursorPos(NewPos) # Como pueden observar la nueva posicion se debe entregar en una lista
        
    def click(self, button):
        """
        El valor de "button" dependera de que boton del mouse quieres que se accione.
        1 = Boton Izquierdo
        2 = Boton Derecho
        
        Vemos que utilizamos el metodo getPosition para decirle en que posición el mouse hara click.
        En este caso, sera en la posición en la que se encuantre el cursor
        """
        clickAction = 2 ** ((2 * button) - 1)
        x = self.getPosition()[0] 
        y = self.getPosition()[1]
        win32api.mouse_event(clickAction, x, y)
        
    def scroll(self, vertical=None, horizontal=None):
        """
        El metodo scrool le dara funcionamiento al scroll del mouse.
        Como pueden apreciar recibe dos argumento: vertical para que el scroll suba o baje.
        horizontal para que se mueva hacia los lados.
        """
        if horizontal is not None:
            horizontal = int(horizontal)
            if horizontal == 0:  # Si horizontal es igual a 0 no pasara nada
                pass
            elif horizontal > 0:  # Scroll hacia la derecha si es positivo
                for _ in range(horizontal):
                    win32api.mouse_event(0x01000, 0, 0, 120, 0)
            else:  # Scroll hacia la izquierda si es negativo
                for _ in range(abs(horizontal)):
                    win32api.mouse_event(0x01000, 0, 0, -120, 0)
        
        if vertical is not None:
            vertical = int(vertical)
            if vertical == 0: # Si vertical tiene valor de 0 no pasara nada
                pass
            elif vertical > 0:  # Scroll sube si es positivo
                for _ in range(vertical):
                    win32api.mouse_event(0x0800, 0, 0, 120, 0)
            else:  # Scroll baja si es negativo
                for _ in range(abs(vertical)):
                    win32api.mouse_event(0x0800, 0, 0, -120, 0)
    
    
```

Bueno, hemos declarado muchos metodos no les parece?. Que tal si probamos el funcionamiento de los metodos previamente definidos?.

Pero antes, quiero mostrarles una cosa, para ello dirijamonos a el archivo "__init__.py".


```python
# winbot/__init__.py

print("Modulo importado exitosamente")

# Le indicamos que al moemnto de importar el modulo winbot, queremos que se importe la clase MouseBot de windows.py
# Esto nos evitara tener que escribir el nombre del archivo "windows.py" cada vez que utilizemos la clase MouseBot
from .windows import MouseBot
```

    Modulo importado exitosamente
    


    ----------------------------------------------------------------------

    ModuleNotFoundError                  Traceback (most recent call last)

    <ipython-input-3-d925c040cea8> in <module>()
          5 # Le indicamos que al moemnto de importar el modulo winbot, queremos que se importe la clase MouseBot de windows.py
          6 # Esto nos evitara tener que escribir el nombre del archivo "windows.py" cada vez que utilizemos la clase MouseBot
    ----> 7 from .windows import MouseBot
    

    ModuleNotFoundError: No module named '__main__.windows'; '__main__' is not a package


Lo que hare sera salir de la carpeta winbot y crear el archivo "winbot_test.py" en el cual probare las funciones de la clase MouseBot.


```python
# winbot_test.py

import winbot
```

    Modulo importado exitosamente
    

Muy bien, como pueden observar, al importar el modulo "winbot" se nos muestra el mensaje escrito anteriormente. No simpre importas un modulo y te aparece un mensaje así, No es cierto?.


```python
# winbot_test.py

import winbot

bot = winbot.MouseBot()

print(dir(bot))

poscursor = bot.getPosition() # posición del cursor
bot.move(145,43) # mover El cursro
bot.click(1) # Hacer Click en el boton izquierdo del mouse
bot.scroll(vertical=-10)
```

    MouseBot se ha inicializado con exito
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'click', 'getPosition', 'move', 'scroll']
    

Como pueden observar, se nos muestra un mensaje indicandonos que la calse MouseBot se ha inicializado con exito. Luego se nos muestran los metodos que posee nuestra clase. Por desgracia no puedo mostrarles lo que la clase es capaz de hacer, pero ustedes mismos pueden realizar este proyecto y ver el resultado directamnete desde tu computador.

Bueno, creo que dejare el articulo hasta aquí y lo finalizaremos luego.

¿Crees que le hace falta lago al modulo? ¿Que le cambiarias? Quiero que me dejes tu comentario dandonos tu opinion.

No te pierdas el proximo articulo en el cual acabaremos el proyecto.

Mi nombre es Luis, y fue un placer compartir mis conocimento con todos ustedes :D.
