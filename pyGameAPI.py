from mysql.connector import connect, Error

import random
import time
import os
import _thread

from pygame.locals import(
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    K_p, K_s,         K_o, K_c, K_n,    
    K_ESCAPE, KEYDOWN, QUIT, K_SPACE)

import pygame as pg

import json
import threading
import datetime
import flask
import socket
from flask import request, jsonify

sw = 500
sh = 500
velo = 0
''' Obter o ip da maquina   '''
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print("Servidor %s em %s " %(hostname, local_ip))

''' iniciando o flask '''
app = flask.Flask(__name__)
#app.config["DEBUG"]=True

try:
    connection = connect(host="localhost",user="root",password="raspberry",database="ini42")
    print(connection)
except Error as e:
    print(e)


global algoEscrito
algoEscrito = False
global texto
texto = ""

@app.route("/")
def documentation():
    return "<!DOCTYPE html><head><title>Guide</title></head><body><h1>Links possíveis para acesso:</h1><dl><dt><b>Cores:</b></dt><dd><ul><li>/black</li><li>/white</li><li>/gray</li><li>/red</li><li>/green</li><li>/blue</li><li>/orange</li><li>/purple</li><li>/pink</li></ul></dd><dt><b>Background color:</b></dt><dd><ul><li>/bg/black</li><li>/bg/white</li><li>/bg/gray</li><li>/bg/red</li><li>/bg/green</li><li>/bg/blue</li><li>/bg/orange</li><li>/bg/purple</li><li>/bg/pink</li></ul></dd><dt><b>Tamanho:</b></dt><dd><ul><li>/size/plus</li><li>/size/minus</li></ul></dd><dt><b>Velocidade:</b></dt><dd><ul><li>/speed/plus</li><li>/speed/minus</li></ul></dd><dt><b>Direção de movimento:</b></dt><dd><ul><li>/direction/1</li><li>/direction/2</li><li>/direction/3</li><li>/direction/4</li></ul></dd></dl><h2>Use as setas do teclado para se movimentar!</h2></body></html>"

##########################################################
#####################OPÇÕES DE CORES#######################
##########################################################
@app.route("/red")
def index1():
    global new_pluto
    new_pluto.troca(255,0,0)
    return jsonify("{'red' : 'ok;'}")


@app.route("/green")
def index2():
    global new_pluto
    new_pluto.troca(0,255,0)
    return jsonify("{'green' : 'ok;'}")

@app.route("/blue")
def index3():
    global new_pluto
    new_pluto.troca(0,0,255)
    return jsonify("{'blue' : 'ok;'}") 

@app.route("/yellow")
def index4():
    global new_pluto
    new_pluto.troca(255,255,0)
    return jsonify("{'yellow' : 'ok;'}")

@app.route("/gray")
def index5():
    global new_pluto
    new_pluto.troca(192,192,192)
    return jsonify("{'gray' : 'ok;'}")

@app.route("/black")
def index6():
    global new_pluto
    new_pluto.troca(0,0,0)
    return jsonify("{'black' : 'ok;'}")

@app.route("/purple")
def index7():
    global new_pluto
    new_pluto.troca(65,0,139)
    return jsonify("{'purple' : 'ok;'}")

@app.route("/pink")
def index8():
    global new_pluto
    new_pluto.troca(199, 86, 219)
    return jsonify("{'pink' : 'ok;'}")

@app.route("/orange")
def index9():
    global new_pluto
    new_pluto.troca(214, 139, 64)
    return jsonify("{'orange' : 'ok;'}")

@app.route("/white")
def index10():
    global new_pluto
    new_pluto.troca(255,255,255)
    return jsonify("{'white' : 'ok;'}")

@app.route("/bg/black")
def index11():
    global bgColor 
    bgColor= (0,0,0)
    screen.fill(bgColor)
    return jsonify("{'bgBlack' : 'ok;'}")

@app.route("/bg/white")
def index12():
    global bgColor 
    bgColor= (255,255,255)
    screen.fill(bgColor)
    return jsonify("{'bgWhite' : 'ok;'}")

@app.route("/bg/red")
def index13():
    global bgColor 
    bgColor= (255,0,0)
    screen.fill(bgColor)
    return jsonify("{'bgRed' : 'ok;'}")

@app.route("/bg/blue")
def index14():
    global bgColor 
    bgColor= (0,0,255)
    screen.fill(bgColor)
    return jsonify("{'bgBlue' : 'ok;'}")

@app.route("/bg/green")
def index15():
    global bgColor 
    bgColor= (0,255,0)
    screen.fill(bgColor)
    return jsonify("{'bgGreen' : 'ok;'}")

@app.route("/bg/yellow")
def index16():
    global bgColor 
    bgColor= (255,255,0)
    screen.fill(bgColor)
    return jsonify("{'bgYellow' : 'ok;'}")

@app.route("/bg/gray")
def index17():
    global bgColor 
    bgColor= (192,192,192)
    screen.fill(bgColor)
    return jsonify("{'bgGray' : 'ok;'}")
    
@app.route("/bg/pink")
def index18():
    global bgColor 
    bgColor= (199, 86, 219)
    screen.fill(bgColor)
    return jsonify("{'bgPink' : 'ok;'}")

@app.route("/bg/purple")
def index19():
    global bgColor 
    bgColor=(65,0,139)
    screen.fill(bgColor)
    return jsonify("{'bgPurple' : 'ok;'}")

@app.route("/bg/orange")
def index20():
    global bgColor 
    bgColor=(214, 139, 64)
    screen.fill(bgColor)
    return jsonify("{'bgOrange' : 'ok;'}")

@app.route("/<red>/<green>/<blue>")
def trocarCor(red,green,blue):
    global new_pluto
    new_pluto.troca(int(red),int(green),int(blue))
    return jsonify("{'cor nova' : 'ok;'}")
    
##########################################################
######################FIM DAS CORES########################
##########################################################



##########################################################
##################CONTROLE DE VELOCIDADE###################
##########################################################
@app.route("/speed/plus")
def index21():
    global new_pluto
    new_pluto.acelera(1)
    return jsonify("{'speed+' : 'ok;'}")

@app.route("/speed/minus")
def index22():
    global new_pluto
    new_pluto.acelera(-1)
    return jsonify("{'speed-' : 'ok;'}")

##########################################################
#####################FIM DA VELOCIDADE#####################
##########################################################



##########################################################
####################CONTROLE DE DIREÇÃO####################
##########################################################
@app.route("/direction/1")
def index23():
    global new_pluto
    new_pluto.direcao = 1
    return jsonify("{'horizontal' : 'ok;'}")

@app.route("/direction/2")
def index24():
    global new_pluto
    new_pluto.direcao = 2
    return jsonify("{'vertical' : 'ok;'}")

@app.route("/direction/3")
def index25():
    global new_pluto
    new_pluto.direcao = 3
    return jsonify("{'diagonal1' : 'ok;'}")

@app.route("/direction/4")
def index26():
    global new_pluto
    new_pluto.direcao = 4
    return jsonify("{'diagonal2' : 'ok;'}")


##########################################################
######################FIM DA DIREÇÃO#######################
##########################################################


##########################################################
###################CONTROLE DE TAMANHO####################
##########################################################


@app.route("/size/plus")
def index27():
    global new_pluto
    return   new_pluto.aumentar(10)

@app.route("/size/minus")
def index28():
    global new_pluto
    return new_pluto.aumentar(-10)

##########################################################
######################FIM DO TAMANHO######################
##########################################################
@app.route("/get")
def getAll():
    comandoSql = "SELECT * FROM pessoa;"
    with connection.cursor() as cursor:
        cursor.execute(comandoSql)
        result = cursor.fetchall()
    for row in result:
        print(row)
    return jsonify(result)



@app.route("/get/<id>")
def getById(id):
    comandoSql = "SELECT * FROM pessoa WHERE id = "+id+";"
    with connection.cursor() as cursor:
        cursor.execute(comandoSql)
        result = cursor.fetchall()
    for row in result:
        print(row)
    return jsonify(result)


@app.route("/insere", methods=['POST'])
def insere():
    print(request.get_json())
    nome = request.get_json()["nome"]
    data = request.get_json()["data"]
    comandoSql = "INSERT INTO pessoa VALUES(null, '"+nome+"', '"+data+"');"
    with connection.cursor() as cursor:
        cursor.execute(comandoSql)
        connection.commit()
    return jsonify("{'insert' : 'ok;'}")

@app.route("/delete/<id>", methods=['GET'])
def chamarThread(id):
    threading.Thread(target=deleta, args=(id)).start()
    

def deleta(id):
    comandoSql = "SELECT nome,data FROM pessoa WHERE id = "+id+";"
    with connection.cursor() as cursor:
        cursor.execute(comandoSql)
        result = cursor.fetchall()
    nome = str(result[0][0])
    data = str(result[0][1])
    global algoEscrito
    algoEscrito = True
    global texto
    texto = nome + " " + data
    comandoSql = "DELETE FROM pessoa WHERE id ="+id+";"
    with connection.cursor() as cursor:
        cursor.execute(comandoSql)
        connection.commit()
    i = 0
    while i <20:
        time.sleep(1)
        algoEscrito = False
        time.sleep(1)
        algoEscrito = True
        i += 2
    algoEscrito = False
    
    return jsonify(result)

def runServer():
     app.run(host=local_ip, port= 5000)

def escrever(texto):
    font = pg.font.Font('freesansbold.ttf',20)
    txt = font.render(str(texto),True,(0,0,0))
    screen.blit(txt,(10,10))


class Pluto(pg.sprite.Sprite):   
    def __init__(self):
        super(Pluto, self).__init__()
        self.size = 100
        self.surf = pg.Surface((self.size, self.size))
        self.surf.fill((255,0,0))        
        self.rect = self.surf.get_rect(
            center =( 250,250
            )  
        )#   surf.get_rect()
        self.speed = velo
        self.sentido = 0
        self.direcao = 1
        
    def update(self, p_keys):

        if(self.direcao == 1):#horizontal
            if self.sentido == 0:
                screen.fill(bgColor)
                self.rect.move_ip(-self.speed,0)
            if self.sentido == 1:
                screen.fill(bgColor)
                self.rect.move_ip(self.speed, 0)
            if self.rect.right < self.size:
                self.sentido = 1
            if self.rect.right > 500:
                self.sentido = 0

        if(self.direcao == 2):#vertical
            if self.sentido == 0:
                screen.fill(bgColor)
                self.rect.move_ip(0,-self.speed)
            if self.sentido == 1:
                screen.fill(bgColor)
                self.rect.move_ip(0,self.speed)
            if self.rect.bottom < self.size:
                self.sentido = 1
            if self.rect.bottom > 500:
                self.sentido = 0
        
        if(self.direcao == 3):#diagonal principal
            if self.sentido == 0:
                screen.fill(bgColor)
                self.rect.move_ip(-self.speed,-self.speed)
            if self.sentido == 1:
                screen.fill(bgColor)
                self.rect.move_ip(self.speed,self.speed)
            if self.rect.bottom < self.size:
                self.sentido = 1
            if self.rect.bottom > 500:
                self.sentido = 0
            if self.rect.right < self.size:
                self.sentido = 1
            if self.rect.right > 500:
                self.sentido = 0

        if(self.direcao == 4):#diagonal secundaria
            if self.sentido == 0:
                screen.fill(bgColor)
                self.rect.move_ip(self.speed,-self.speed)
            if self.sentido == 1:
                screen.fill(bgColor)
                self.rect.move_ip(-self.speed,self.speed)
            if self.rect.bottom < self.size:
                self.sentido = 1
            if self.rect.bottom > 500:
                self.sentido = 0
            if self.rect.right < self.size:
                self.sentido = 0
            if self.rect.right > 500:
                self.sentido = 1

    def moverSetas(self, valor):
        if valor == 0:
            if self.rect.bottom <= self.size:
                return
            screen.fill(bgColor)
            self.rect.move_ip(0,-10)
        if valor == 1:
            if self.rect.right <= self.size:
                return
            screen.fill(bgColor)
            self.rect.move_ip(-10,0)
        if valor == 2:
            if self.rect.right >= 500:
                return
            screen.fill(bgColor)
            self.rect.move_ip(10,0)
        if valor == 3:
            if self.rect.bottom >= 500:
                return
            screen.fill(bgColor)
            self.rect.move_ip(0,10)
    
    
    def aumentar(self,valor):
        if(self.size >= 500 and valor > 0):
            return jsonify("{'MAX SIZE-' : 'ERROR'}")
        if(self.size <= 0 and valor < 0):
           return jsonify("{'MIN SIZE-' : 'ERROR'}")
        self.rect.inflate_ip(valor,valor)
        self.size += valor
        self.surf = pg.Surface((self.size, self.size))
        self.troca(255,0,0)
        return jsonify("{'size' : 'ok'}")
        

    def draw(self, surface):
        surface.blit(self.surf,self.rect)

    def troca(self, r,g,b):
        self.surf.fill((r, g ,b))

    def acelera(self,valor):
        if self.speed == 0 and valor<0:
            return
        self.speed += valor
        
    


# inicia a tela em um determinada posicao....
x = 200
y = 200
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

ADDPLUTO = pg.USEREVENT + 1
SONG_END = ADDPLUTO + 1
TEST_EVENT = SONG_END + 1

my_event = pg.event.Event(TEST_EVENT, message="teste")

_thread.start_new_thread(runServer,())

#criando cores no python
bgColor = (255,255,255)
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((sw,sh))

plutos = pg.sprite.Group()
new_pluto = Pluto()
plutos.add(new_pluto)
all_sprites = pg.sprite.Group()
all_sprites.add(plutos)

screen.fill(bgColor)

running = True
while running:
  # pegar evento do X de fechar janela
    for event in pg.event.get():
        if event.type == KEYDOWN:
          # verifico qual tecla apertada 
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_UP:
                new_pluto.moverSetas(0)
            if event.key == K_DOWN:
                new_pluto.moverSetas(3)
            if event.key == K_RIGHT:
                new_pluto.moverSetas(2)
            if event.key == K_LEFT:
                new_pluto.moverSetas(1)
            
        elif event.type == pg.QUIT:
            running = False 
        elif event.type == TEST_EVENT:
            print(event.message)
            print('Evento acionado')
            print(velo)
            
    keyp = pg.key.get_pressed()
    
    all_sprites.update(keyp)
    if algoEscrito == 1:
        escrever(texto)
    
    for entity in all_sprites:
        entity.draw(screen)
        
    pg.display.flip()
    clock.tick(100)


pg.quit()