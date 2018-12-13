from visao.src.detector import DetectorX
from tictactoe.minmaxtoe import MinMaxToe
import cv2
import numpy as np


class RoboJogoVelha:

    def __init__(self, *args, **kwargs):
        if isinstance(args[0], str) and len(args[0]) == 1:
            self.jogo = MinMaxToe(args[0])
        else:
            self.jogo = MinMaxToe(kwargs.get('jogador', 'X'))
        # Não vamos passar uma imagem para o construtor pois a detecção sera feita realizando o
        # particionamento da imagem no metodo analisar_partes
        self.visao = DetectorX(None, './visao/resources/svms/smvX.svm')
        self.cam = cv2.VideoCapture(0)
        self.lista_partes = []
        self.largura_parte = self.altura_parte = 0

    def calcular_partes(self):
        imagem = self.cam.read()[1]
        largura, altura = imagem.shape[:2]
        largura_div = largura / 3
        altura_div = altura / 3
        lista_partes = []
        for x in range(3):
            x_parte = largura_div * x
            for y in range(3):
                y_parte = altura_div * y
                lista_partes.append([x_parte, y_parte, 0])
        self.lista_partes = lista_partes
        self.largura_parte = largura_div
        self.altura_parte = altura_div

    def analisar_parte(self, indice: int) -> bool:
        x_ini = int(self.lista_partes[indice][0])
        x_end = int(x_ini + self.largura_parte)
        y_ini = int(self.lista_partes[indice][1])
        y_end = int(y_ini + self.altura_parte)
        imagem = self.cam.read()[1]
        parte = imagem[x_ini:x_end, y_ini:y_end]
        return self.visao.detectar(parte)

    def procurar_ultima_jogada(self):
        for c in range(len(robo.lista_partes)):
            if robo.lista_partes[c][2] == 0:
                analise = robo.analisar_parte(c)
                if analise is True:
                    pos_mov = robo.jogo.posicoes[c]
                    if pos_mov in robo.jogo.esp_livres():
                        robo.lista_partes[c][2] = MinMaxToe.JOGADOR
                        return c
        return None

    def exibi_visao(self):
        imagem_visao = self.cam
        for p in self.lista_partes:
            esq = p[0]
            drt = esq + self.largura_parte
            topo = [1]
            baixo = topo + self.altura_parte
            if p[2] == MinMaxToe.JOGADOR:
                cv2.rectangle(imagem_visao, (esq, topo), (drt, baixo), DetectorX.COR_VERDE, 2)
            elif p[2] == MinMaxToe.COMPUTADOR:
                cv2.rectangle(imagem_visao, (esq, topo), (drt, baixo), DetectorX.COR_AZUL, 2)


if __name__ == '__main__':
    robo = RoboJogoVelha('X')
    robo.calcular_partes()
    while not robo.jogo.fim_jogo():
        pos = robo.procurar_ultima_jogada()
        while pos is None:
            input("Erro ao procurar ultima jogada, pressione enter para tentar novamente!")
            pos = robo.procurar_ultima_jogada()
        pos_mov = robo.jogo.posicoes[pos]
        robo.jogo.realiza_mov(MinMaxToe.JOGADOR, pos_mov)
        mov_robo = robo.jogo.mv_computador()
        robo.lista_partes[mov_robo][MinMaxToe.COMPUTADOR]
        robo.exibir_visao()
    print('Vencedor: {}'.format(robo.jogo.obter_vencedor()))
