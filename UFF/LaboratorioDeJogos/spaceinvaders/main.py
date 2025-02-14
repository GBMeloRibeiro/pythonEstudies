import dificuldade
import ranking

from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
import dificuldade
import ranking

janela = Window(900,600)
janela.set_title("Menu Principal")
teclado = Keyboard()
fundo= GameImage("background.jpg")
mouse= Window.get_mouse()

#definindo botoes 200 x 60
botao1 = Sprite("botao.png")
botao2 = Sprite("botao.png")
botao3 = Sprite("botao.png")
botao4 = Sprite("botao.png")

botao1.set_position(janela.width/2 - 100, 175)
botao2.set_position(janela.width/2 - 100, 275)
botao3.set_position(janela.width/2 - 100, 375)
botao4.set_position(janela.width/2 - 100, 475)

def principal(): #função para retornar do menu

    fundo.draw()
    # faz os botoes aparecerem na tela
    botao1.draw()
    botao2.draw()
    botao3.draw()
    botao4.draw()

    # Define o nome dos botões no menu
    janela.draw_text(f"MENU", janela.width / 2 - 105, 60, size=73, color=(255, 255, 255))
    janela.draw_text(f"JOGAR", janela.width / 2 - 60, 190, size=30, color=(0, 0, 0))
    janela.draw_text(f"DFICULDADE", janela.width / 2 - 85, 294, size=25, color=(0, 0, 0))
    janela.draw_text(f"RANKING", janela.width / 2 - 73, 390, size=30, color=(0, 0, 0))
    janela.draw_text(f"SAIR", janela.width / 2 - 50, 490, size=30, color=(0, 0, 0))

def menu_principal(jogar_func):
    while True:

        fundo.draw()
        principal()

        #verifica a localização do mouse
        if mouse.is_over_area((botao1.x, botao1.y), (botao1.x + botao1.width, botao1.y + botao1.height)):
            if mouse.is_button_pressed(1):
                jogar_func() #chamar a função jogar

        if mouse.is_over_area((botao2.x, botao2.y), (botao2.x + botao2.width, botao2.y + botao2.height)):
            if mouse.is_button_pressed(1):
                dificuldade.dificuldade() #chama a função dificuldade

        if mouse.is_over_area((botao3.x, botao3.y), (botao3.x + botao3.width, botao3.y + botao3.height)):
            if mouse.is_button_pressed(1):
                ranking.ranking() #chama a função ranking

        if mouse.is_over_area((botao4.x, botao4.y), (botao4.x + botao4.width, botao4.y + botao4.height)):
            if mouse.is_button_pressed(1):
                janela.close() #break

        janela.update()

if __name__== "__main__": #chamando o modo jogo
    import jogar
    menu_principal(jogar.jogar)
