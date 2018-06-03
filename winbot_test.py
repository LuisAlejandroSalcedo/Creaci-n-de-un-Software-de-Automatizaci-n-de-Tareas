# winbot_test.py

import winbot

bot = winbot.MouseBot()

print(dir(bot))

poscursor = bot.getPosition() # posición del cursor
bot.move(145,43) # mover El cursro
bot.click(1) # Hacer Click en el boton izquierdo del mouse
bot.scroll(vertical=-10)