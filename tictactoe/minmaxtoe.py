from math import inf as infinito
from random import randint


class MinMaxToe:
    JOGADOR = -1
    COMPUTADOR = 1

    def __init__(self, simb_jogador):
        self.tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.posicoes = [[0, 0], [0, 1], [0, 2],
                         [1, 0], [1, 1], [1, 2],
                         [2, 0], [2, 1], [2, 2]]
        self.simb_jogador = simb_jogador

    def minmax(self, indice, player):
        """
        Função recursiva para o calculo de todas as jogadas possiveis e encontrar a melhor dentre elas.
        :param indice: posição a ser jogada
        :param player: jogador ou computador (-1 ou 1)
        :return:
        """
        melhor_jogada = []
        if player == MinMaxToe.COMPUTADOR:
            melhor_jogada = [-1, -1, -infinito]  # para o computador, quanto maior o valor da posicao 1, melhor.
        else:
            melhor_jogada = [-1, -1, infinito]  # para o jogador, quanto menor o valor da posicao 1, melhor.

        if indice == 0 or self.fim_jogo():
            resultado = self.obter_vencedor()  # Vetor usado para comparação recursiva
            return [-1, -1, resultado]

        # Laço para calcular cada jogada possivel dentre as posições livres
        for pos in self.esp_livres():
            x, y = pos[0], pos[1]
            self.tabuleiro[x][y] = player
            # Recursividade
            resultado = self.minmax(indice - 1, -player)
            self.tabuleiro[x][y] = 0
            resultado[0], resultado[1] = x, y

            if player == MinMaxToe.COMPUTADOR:
                if resultado[2] > melhor_jogada[2]:
                    melhor_jogada = resultado
            else:
                if resultado[2] < melhor_jogada[2]:
                    melhor_jogada = resultado
        return melhor_jogada

    def obter_vencedor(self):
        """
        Verifica se existe um vencedor.
        :return: 1 se o computador for vencedor, -1 se o jogador for vencecdor, 0 se empatar
        """
        if self.verificar_vencedor(MinMaxToe.COMPUTADOR):
            vencedor = MinMaxToe.COMPUTADOR
        elif self.verificar_vencedor(MinMaxToe.JOGADOR):
            vencedor = MinMaxToe.JOGADOR
        else:
            vencedor = 0
        return vencedor

    def verificar_vencedor(self, player):
        """
        Essa funcão verifica a existencia de um ganhador
        :param player: jogador a ser analizado
        :return: True se player é o vencedor, False se não é vencedor
        """
        combos = [
            [self.tabuleiro[0][0], self.tabuleiro[0][1], self.tabuleiro[0][2]],
            [self.tabuleiro[1][0], self.tabuleiro[1][1], self.tabuleiro[1][2]],
            [self.tabuleiro[2][0], self.tabuleiro[2][1], self.tabuleiro[2][2]],
            [self.tabuleiro[0][0], self.tabuleiro[1][0], self.tabuleiro[2][0]],
            [self.tabuleiro[0][1], self.tabuleiro[1][1], self.tabuleiro[2][1]],
            [self.tabuleiro[0][2], self.tabuleiro[1][2], self.tabuleiro[2][2]],
            [self.tabuleiro[0][0], self.tabuleiro[1][1], self.tabuleiro[2][2]],
            [self.tabuleiro[2][0], self.tabuleiro[1][1], self.tabuleiro[0][2]],
        ]
        if [player, player, player] in combos:
            return True
        else:
            return False

    def fim_jogo(self):
        """
        Essa função verifica se o jogo acabou
        :return: True se o jogo acabou.
        """
        return self.verificar_vencedor(MinMaxToe.COMPUTADOR) \
               or self.verificar_vencedor(MinMaxToe.JOGADOR) \
               or len(self.esp_livres()) == 0

    def esp_livres(self):
        """
        :return: Retorna uma lista com as posições livres do tabuleiro
        """
        pos_disponiveis = []
        # Relaciona cada numero correspondente a uma posição do tabuleiro com o valor que esta naquela posicao
        for x, linha in enumerate(self.tabuleiro):
            for y, celula in enumerate(linha):
                if celula == 0: pos_disponiveis.append([x, y])
        return pos_disponiveis

    def validar_mov(self, pos):
        """
        Verifica se a posição em que deseja jogar é uma posição livre no tabuleiro
        :param pos: posição que se deseja jogar
        :return: True se for uma posição livre.
        """
        if pos in self.esp_livres():
            return True
        return False

    def realiza_mov(self, player, pos):
        """
        Se a posicao recebida for uma posição livre no tabuleiro, realiza o movimento.
        :param player: jogador ou computador
        :param pos: posição do tabuleiro
        :return: True se o movimento for valido.
        """
        if player == MinMaxToe.JOGADOR and isinstance(pos, int):
            pos = self.posicoes[pos]
        if self.validar_mov(pos):
            self.tabuleiro[pos[0]][pos[1]] = player
            return True
        return False

    def exibir(self):
        """
        Printa o tabuleiro no console
        :return:
        """
        img_tab = '-------\n'
        for linha in self.tabuleiro:
            for celula in linha:
                img_tab += '|{}'.format(celula)
            img_tab += '|\n'
            img_tab += '-------\n'
        if self.simb_jogador == 'X':
            simb_comp = 'O'
        else:
            simb_comp = 'X'
        img_tab = img_tab.replace(str(MinMaxToe.JOGADOR), self.simb_jogador)
        img_tab = img_tab.replace(str(MinMaxToe.COMPUTADOR), simb_comp)
        print(img_tab)

    def mv_computador(self) -> int:
        """
        Realiza o movimento do computador automaticamente
        utilizando o metodo minimax.
        :return: True se o pos_mov foi realizado.
        """
        possibilidades = len(self.esp_livres())
        if possibilidades == 0 or self.fim_jogo():
            return False
        if possibilidades == 9:
            self.realiza_mov(MinMaxToe.COMPUTADOR, randint(0, 8))

        pos_mov = self.minmax(possibilidades, MinMaxToe.COMPUTADOR)
        self.realiza_mov(MinMaxToe.COMPUTADOR, pos_mov[0:2])
        return pos_mov
