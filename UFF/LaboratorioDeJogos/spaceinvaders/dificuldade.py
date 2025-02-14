from  PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import main
def dificuldade():

    #abrir janela e definir fundo
    mdificuldad= Window(900,600)
    fundo= GameImage("background.jpg")

    #inicialização dos botões
    botao1 = Sprite("botao.png")
    botao2 = Sprite("botao.png")
    botao3 = Sprite("botao.png")

    #posicionando os botoes
    botao1.set_position(mdificuldad.width / 2 - 100, 175)
    botao2.set_position(mdificuldad.width / 2 - 100, 275)
    botao3.set_position(mdificuldad.width / 2 - 100, 375)

    #chamando teclado e mousee
    teclado= Window.get_keyboard()
    mouse = Window.get_mouse()

    #modo standard de difiuldade
    dificult = 1

    while True:

        fundo.draw()
        # desenhar botoes
        botao1.draw()
        botao2.draw()
        botao3.draw()
        #back
        if teclado.key_pressed("ESC"):
            main.principal()
            break

        mdificuldad.draw_text(f"FÁCIL", mdificuldad.width / 2 - 55, 189, size=30, color=(0, 0, 0))
        mdificuldad.draw_text(f"MÉDIO", mdificuldad.width / 2 - 60, 289, size=30, color=(0, 0, 0))
        mdificuldad.draw_text(f"DIFÍCIL", mdificuldad.width / 2 - 55, 389, size=30, color=(0, 0, 0))

        #verifica onde o mouse esta
        if mouse.is_over_area((botao1.x, botao1.y), (botao1.x + botao1.width, botao1.y + botao1.height)):
            if mouse.is_button_pressed(1): #easy
                dificult = 1
        elif mouse.is_over_area((botao2.x, botao2.y), (botao2.x + botao2.width, botao2.y + botao2.height)):
            if mouse.is_button_pressed(1): #medium
                dificult = 2
        elif mouse.is_over_area((botao3.x, botao3.y), (botao3.x + botao3.width, botao3.y + botao3.height)):
            if mouse.is_button_pressed(1): #hard
                dificult = 3


        mdificuldad.update()