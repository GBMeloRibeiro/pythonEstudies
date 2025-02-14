import main
from PPlay.window import *
from PPlay.gameimage import *

def exibir_ranking_na_tela(tela):
    try:
        with open("ranking.txt", "r") as arquivo:
            dados = [linha.strip().split(",") for linha in arquivo.readlines()]
            dados.sort(key=lambda x: int(x[1]), reverse=True)

            tela.draw_text("Ranking dos Melhores Jogadores", 300, 50, size=32, color=(255, 255, 255), bold=True)

            for i, (nome, pontuacao, data) in enumerate(dados[:5]):
                tela.draw_text(f"{i + 1}. {nome} - Pontuação: {pontuacao} - Data: {data}", 100, 120 + i * 40, size=24, color=(255, 255, 255))
    except FileNotFoundError:
        tela.draw_text("Nenhum ranking encontrado!", 300, 300, size=24, color=(255, 255, 255))

def ranking():
    tela = Window(900, 600)
    tela.set_title("Ranking")
    teclado = Window.get_keyboard()

    while True:
        tela.set_background_color((0, 0, 0))  # Fundo preto
        exibir_ranking_na_tela(tela)

        # Voltar ao menu principal
        if teclado.key_pressed("ESC"):
            main.principal()
            break

        tela.update()
