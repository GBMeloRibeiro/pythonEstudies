from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
import random
import time
from datetime import datetime

# Configuração da janela e elementos principais
janela = Window(900, 600)
teclado = Keyboard()
cenario = GameImage("background.jpg")
jogador = GameImage("nave.png")
jogador.x = janela.width / 2.35
jogador.y = janela.height / 1.2
tiros = []
tiros_inimigos = []
tempo_recarga = 0.5
tempo_desde_ultimo_tiro = 0
linhas_inimigos = 6
colunas_inimigos = 3
inimigo = []
vidas = 3
invencivel = False
tempo_invencibilidade = 2
ultimo_tempo_invencivel = 0
fase = 1
pontuacao = 0

# Função para reiniciar posição do jogador
def reset_jogador():
    jogador.x = janela.width / 2.35
    jogador.y = janela.height / 1.2

# Função para criar uma nova horda de inimigos
def criar_inimigos(fase):
    inimigo.clear()
    for linha in range(linhas_inimigos):
        linha_inimigo = []
        for coluna in range(colunas_inimigos):
            elemento = GameImage("inimigo.png")
            elemento.set_position(100 + linha * 60, 50 + coluna * 50)
            linha_inimigo.append(elemento)
        inimigo.append(linha_inimigo)

# Inicializar primeira horda
criar_inimigos(fase)

# Função para salvar ranking
def salvar_ranking(nome, pontuacao):
    with open("ranking.txt", "a") as arquivo:
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo.write(f"{nome},{pontuacao},{data}\n")

# Função para exibir o ranking
def exibir_ranking():
    try:
        with open("ranking.txt", "r") as arquivo:
            dados = [linha.strip().split(",") for linha in arquivo.readlines()]
            dados.sort(key=lambda x: int(x[1]), reverse=True)
            print("Ranking dos 5 melhores jogadores:")
            for i, (nome, pontuacao, data) in enumerate(dados[:5]):
                print(f"{i + 1}. {nome} - Pontuação: {pontuacao} - Data: {data}")
    except FileNotFoundError:
        print("Nenhum ranking encontrado!")

def jogar():
    global tempo_desde_ultimo_tiro, pontuacao, vidas, invencivel, ultimo_tempo_invencivel, fase
    velocidade_inimigos = 50
    direcao_inimigos = 1
    descida_inimigos = 20
    tempo_movimento_inimigos = 1.0
    ultimo_movimento_inimigos = time.time()
    tempo_tiro_inimigo = 1.5
    ultimo_tiro_inimigo = time.time()

    while True:
        if time.time() - ultimo_movimento_inimigos > tempo_movimento_inimigos:
            mover_inimigos = True
            for linha_inimigo in inimigo:
                for elemento in linha_inimigo:
                    elemento.x += velocidade_inimigos * direcao_inimigos
                    if elemento.x + elemento.width >= janela.width or elemento.x <= 0:
                        mover_inimigos = False
            if not mover_inimigos:
                direcao_inimigos *= -1
                for linha_inimigo in inimigo:
                    for elemento in linha_inimigo:
                        elemento.y += descida_inimigos
            ultimo_movimento_inimigos = time.time()

        deltatime = janela.delta_time()
        tempo_desde_ultimo_tiro += deltatime

        # Desenho do cenário
        cenario.draw()

        # Movimento do jogador
        if teclado.key_pressed("LEFT") and jogador.x > 0:
            jogador.x -= 200 * deltatime
        if teclado.key_pressed("RIGHT") and jogador.x < (janela.width - jogador.width):
            jogador.x += 200 * deltatime

        # Tiros do jogador
        if teclado.key_pressed("SPACE") and tempo_desde_ultimo_tiro >= tempo_recarga:
            novo_tiro = GameImage("tiro.png")
            novo_tiro.x = jogador.x + jogador.width / 2 - novo_tiro.width / 2
            novo_tiro.y = jogador.y
            tiros.append(novo_tiro)
            tempo_desde_ultimo_tiro = 0

        # Movimento e remoção de tiros do jogador
        for tiro in tiros[:]:
            tiro.y -= 300 * deltatime
            tiro.draw()
            if tiro.y + tiro.height < 0:
                tiros.remove(tiro)

        # Movimento e remoção de tiros dos inimigos
        for tiro in tiros_inimigos[:]:
            tiro.y += 200 * deltatime
            tiro.draw()
            if tiro.y > janela.height:
                tiros_inimigos.remove(tiro)

        # Colisão dos tiros com os inimigos
        for tiro in tiros[:]:
            for linha_inimigo in inimigo:
                for elemento in linha_inimigo[:]:
                    if tiro.collided(elemento):
                        tiros.remove(tiro)
                        linha_inimigo.remove(elemento)
                        pontuacao += 100
                        break

        # Colisão dos tiros inimigos com o jogador
        if not invencivel:
            for tiro in tiros_inimigos[:]:
                if tiro.collided(jogador):
                    tiros_inimigos.remove(tiro)
                    vidas -= 1
                    if vidas > 0:
                        invencivel = True
                        ultimo_tempo_invencivel = time.time()
                        reset_jogador()
                    else:
                        print("Fim de jogo! Insira seu nome para o ranking: ")
                        nome = input("Nome: ")
                        salvar_ranking(nome, pontuacao)
                        return

        # Efeito de invencibilidade do jogador
        if invencivel:
            if time.time() - ultimo_tempo_invencivel > tempo_invencibilidade:
                invencivel = False
            elif int((time.time() - ultimo_tempo_invencivel) * 5) % 2 == 0:
                jogador.draw()
        else:
            jogador.draw()

        # Desenho dos inimigos e geração de tiros aleatórios
        for linha_inimigo in inimigo:
            for elemento in linha_inimigo:
                elemento.draw()
                if time.time() - ultimo_tiro_inimigo > tempo_tiro_inimigo + random.uniform(0, 1):
                    novo_tiro = GameImage("tiro.png")
                    novo_tiro.x = elemento.x + elemento.width / 2 - novo_tiro.width / 2
                    novo_tiro.y = elemento.y + elemento.height
                    tiros_inimigos.append(novo_tiro)
                    ultimo_tiro_inimigo = time.time()

        # Verificar se todos os inimigos foram derrotados
        if all(not linha_inimigo for linha_inimigo in inimigo):
            fase += 1
            #linhas_inimigos += 1
            criar_inimigos(fase)
            velocidade_inimigos += 10
            tempo_movimento_inimigos *= 0.9

        # Exibição da pontuação e vidas
        janela.draw_text(f"Pontuação: {pontuacao}", 10, 10, size=24, color=(255, 255, 255), bold=True)
        janela.draw_text(f"Vidas: {vidas}", 10, 40, size=24, color=(255, 255, 255), bold=True)
        janela.draw_text(f"Fase: {fase}", 10, 70, size=24, color=(255, 255, 255), bold=True)

        # Atualização da janela
        janela.update()

        # Botão para exibir ranking
        if teclado.key_pressed("R"):
            exibir_ranking()

        # Sair do jogo
        if teclado.key_pressed("ESC"):
            break

jogar()
