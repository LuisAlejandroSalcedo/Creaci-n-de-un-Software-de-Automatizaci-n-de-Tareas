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
    
    