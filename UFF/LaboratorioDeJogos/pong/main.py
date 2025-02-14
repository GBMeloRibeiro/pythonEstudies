from PPlay.window import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.keyboard import *
janela = Window(1051, 626)
cenario = GameImage("background.jpg")
bola = GameImage("ball.png")
jogador = GameImage("barra.jpg")
computador = GameImage("barra.jpg")
bola.x = janela.width/2 - bola.width/2
bola.y = janela.height/2 - bola.height/2
jogador.x = 1031
jogador.y = janela.height/2
computador.x = 5
computador.y = janela.height/2
velx = 5
vely = 1 
velcomputador = 3
teclado = Keyboard()
pausado = False
def mudar_direcao(barra, bola):
    acerto = (bola.y + bola.width / 2) - (barra.y + barra.height / 2)
    angulo_max = 3
    bola_vel_y = angulo_max * (acerto / (barra.height / 2))
    return bola_vel_y
contjogador = 0
contcomputador = 0
while True:
    bola.x += velx
    bola.y += vely
    if teclado.key_pressed("UP") and jogador.y>0:
        jogador.y-=10
    if teclado.key_pressed("DOWN") and jogador.y<1051:
        jogador.y+=10
    if computador.y + computador.height // 2 < bola.y:
        computador.y += velcomputador
    if computador.y + computador.height // 2 > bola.y:
        computador.y -= velcomputador
    if bola.x >= 1051-bola.width:
        contcomputador += 1
        bola.x = janela.width/2 - bola.width/2
        velx = 5
        vely = 1
        pausado = True
    if bola.x <= 0:
        contjogador += 1
        bola.x = janela.width/2 - bola.width/2
        velx = 5
        vely = 1
        pausado = True
    if bola.y >= 626-bola.height:
        vely = vely*-1.2
    if bola.y <= 0:
        vely = vely*-1.2
    #if bola.collided(jogador) or bola.collided(computador):
    #velx = velx*-1.2
    #vely = vely*-1.2
    if bola.collided(jogador):
            velx *= -1.2
            vely = mudar_direcao(jogador, bola)

    elif bola.collided(computador):
            velx *= -1.2
            vely = mudar_direcao(computador, bola)
    cenario.draw()
    bola.draw()
    jogador.draw()
    computador.draw()
    janela.draw_text(f"{contcomputador} | {contjogador}", janela.width / 2 - 70, 10, size=60, color=(255, 255, 255))
    if pausado:
        velx = 0
        vely = 0
        janela.draw_text("Pressione ESPAÇO para começar", janela.width / 2 - 310, janela.height/ 2 - 20, size=40, color=(255, 255, 255))
        janela.update()
        if teclado.key_pressed("SPACE"):
            pausado = False
            velx = 5
    janela.update()
