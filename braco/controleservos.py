from time import sleep
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685


class ControleServos:
    # Declaração dos vetores de posições do tabuleiro
    REPOUSO = [90, 90, 10]
    MARCA_1 = [43, 38, 115]
    MARCA_2 = [90, 40, 138]
    MARCA_3 = [145, 38, 105]
    MARCA_4 = [50, 30, 68]
    MARCA_5 = [90, 36, 98]
    MARCA_6 = [125, 29, 62]
    MARCA_7 = [62, 16, 20]
    MARCA_8 = [90, 20, 30]
    MARCA_9 = [112, 16, 20]
    PECA1 = [[6, 54, 148], [6, 37, 117], [6, 49, 132]]
    PECA2 = [[4, 28, 65], [4, 20, 44], [4, 33, 60]]
    PECA3 = [[24, 19, 25], [24, 7, 35], [24, 27, 44]]
    PECA4 = [[176, 38, 104], [176, 34, 100], [176, 49, 122]]
    PECA5 = [[159, 13, 15], [159, 9, 9], [159, 25, 40]]
    # Vetor motores, composto por [num_porta_pwm, pos_escrita, pos_desejada]
    # valores do angulo da garra para abrir e pegar peças.
    ABRE = 50
    FECHA = 10
    # valor em graus para subir suavemente
    SOBE = 30

    def __init__(self):
        # Cria a interface I2C padrao
        i2c = busio.I2C(SCL, SDA)

        # Cria uma instancia de PCA9685 passando como parametro a interface I2C padrao (0x40)
        self.pca = PCA9685(i2c)

        # Set the PWM frequency to 60hz.
        self.pca.frequency = 60

        self.mot0 = [0, ControleServos.REPOUSO[0], ControleServos.REPOUSO[0]]
        self.mot1 = [4, ControleServos.REPOUSO[1], ControleServos.REPOUSO[1]]
        self.mot2 = [8, ControleServos.REPOUSO[2], ControleServos.REPOUSO[2]]
        self.garra = 12

    def realizar_movimento(self, numero_mov):
        if 0:
            # posicao de repouspo
            self.ctrlMotor(ControleServos.REPOUSO[0], ControleServos.REPOUSO[1], ControleServos.REPOUSO[2])
        # posicoes correspondentes a uma posicao do tabuleiro
        elif numero_mov == 1:
            self.ctrlMotor(ControleServos.MARCA_1[0], ControleServos.MARCA_1[1], ControleServos.MARCA_1[2])
        elif numero_mov == 2:
            self.ctrlMotor(ControleServos.MARCA_2[0], ControleServos.MARCA_2[1], ControleServos.MARCA_2[2])
        elif numero_mov == 3:
            self.ctrlMotor(ControleServos.MARCA_3[0], ControleServos.MARCA_3[1], ControleServos.MARCA_3[2])
        elif numero_mov == 4:
            self.ctrlMotor(ControleServos.MARCA_4[0], ControleServos.MARCA_4[1], ControleServos.MARCA_4[2])
        elif numero_mov == 5:
            self.ctrlMotor(ControleServos.MARCA_5[0], ControleServos.MARCA_5[1], ControleServos.MARCA_5[2])
        elif numero_mov == 6:
            self.ctrlMotor(ControleServos.MARCA_6[0], ControleServos.MARCA_6[1], ControleServos.MARCA_6[2])
        elif numero_mov == 7:
            self.ctrlMotor(ControleServos.MARCA_7[0], ControleServos.MARCA_7[1], ControleServos.MARCA_7[2])
        elif numero_mov == 8:
            self.ctrlMotor(ControleServos.MARCA_8[0], ControleServos.MARCA_8[1], ControleServos.MARCA_8[2])
        elif numero_mov == 9:
            self.ctrlMotor(ControleServos.MARCA_9[0], ControleServos.MARCA_9[1], ControleServos.MARCA_9[2])
        # Posicoes para pegar as PECAs. 10 = se aproximar, 11 = pegar, 12 = fastar
        elif numero_mov == 10:
            self.ctrlMotor(ControleServos.PECA1[0][0], ControleServos.PECA1[0][1], ControleServos.PECA1[0][2])
        elif numero_mov == 11:
            self.ctrlMotor(ControleServos.PECA1[1][0], ControleServos.PECA1[1][1], ControleServos.PECA1[1][2])
        elif numero_mov == 12:
            self.ctrlMotor(ControleServos.PECA1[2][0], ControleServos.PECA1[2][1], ControleServos.PECA1[2][2])
        elif numero_mov == 20:
            self.ctrlMotor(ControleServos.PECA2[0][0], ControleServos.PECA2[0][1], ControleServos.PECA2[0][2])
        elif numero_mov == 21:
            self.ctrlMotor(ControleServos.PECA2[1][0], ControleServos.PECA2[1][1], ControleServos.PECA2[1][2])
        elif numero_mov == 22:
            self.ctrlMotor(ControleServos.PECA2[2][0], ControleServos.PECA2[2][1], ControleServos.PECA2[2][2])
        elif numero_mov == 30:
            self.ctrlMotor(ControleServos.PECA3[0][0], ControleServos.PECA3[0][1], ControleServos.PECA3[0][2])
        elif numero_mov == 31:
            self.ctrlMotor(ControleServos.PECA3[1][0], ControleServos.PECA3[1][1], ControleServos.PECA3[1][2])
        elif numero_mov == 32:
            self.ctrlMotor(ControleServos.PECA3[2][0], ControleServos.PECA3[2][1], ControleServos.PECA3[2][2])
        elif numero_mov == 40:
            self.ctrlMotor(ControleServos.PECA4[0][0], ControleServos.PECA4[0][1], ControleServos.PECA4[0][2])
        elif numero_mov == 41:
            self.ctrlMotor(ControleServos.PECA4[1][0], ControleServos.PECA4[1][1], ControleServos.PECA4[1][2])
        elif numero_mov == 42:
            self.ctrlMotor(ControleServos.PECA4[2][0], ControleServos.PECA4[2][1], ControleServos.PECA4[2][2])
        elif numero_mov == 50:
            self.ctrlMotor(ControleServos.PECA5[0][0], ControleServos.PECA5[0][1], ControleServos.PECA5[0][2])
        elif numero_mov == 51:
            self.ctrlMotor(ControleServos.PECA5[1][0], ControleServos.PECA5[1][1], ControleServos.PECA5[1][2])
        elif numero_mov == 52:
            self.ctrlMotor(ControleServos.ECA5[2][0], ControleServos.PECA5[2][1], ControleServos.PECA5[2][2])
        # Fechar a garra
        elif numero_mov == 13:
            self.moverMotor(self.garra, ControleServos.ABRE)
        # a brir a garra
        elif numero_mov == 14:
            self.moverMotor(self.garra, ControleServos.FECHA)
        # Levantar
        elif numero_mov == 101:
            self.moverMotor(self.mot2[0], ControleServos.SOBE)

    def ctrlMotor(self, pos_motor1, pos_motor2, pos_motor3):
        # Modifica a pos_desejada de cada vetor motor.
        self.mot0[2] = pos_motor1
        self.mot1[2] = pos_motor2
        self.mot2[2] = pos_motor3
        # de controle para o movimento dos motores.
        while (True):
            """
             Enquanto a diferença entre a pos_escrita e a pos_desejada de cada motor for maior que 0, ou seja,
             Enquanto o motor ainda nao tiver alcançado a pos_desejada, diminui ou aumenta o angulo do motor conforme o caso.
            """
            # tratamento do motor 0
            if abs(self.mot0[1] - self.mot0[2]) > 0:
                # Se a pos_escrita for menor que a pos_desejada, aumenta em 1 o valor da pos_escrita
                if self.mot0[1] < self.mot0[2]:
                    self.mot0[1] += 1
                else:
                    # caso contrario, diminui a pos_escrita em 1 unidade.
                    self.mot0[1] -= 1

            # tratamento do motor 1
            if abs(self.mot1[1] - self.mot1[2]) > 0:
                if self.mot1[1] < self.mot1[2]:
                    self.mot1[1] += 1
                else:
                    self.mot1[1] -= 1
            # tratamento do motor 2
            # o motor 2, recebe uma alteração de valor de 2 unidades, pois no nosso caso isso evita travamentos
            if abs(self.mot2[1] - self.mot2[2]) >= 1:
                if self.mot2[1] < self.mot2[2]:
                    self.mot2[1] += 2
                else:
                    self.mot2[1] -= 2
                # Verifica se nao existe diferença entre a pos_escrita e pos_desejada de cada um dos motores
                if abs(self.mot0[1] - self.mot0[2]) == 0 and abs(self.mot1[1] - self.mot1[2]) == 0 \
                        and abs(self.mot2[1] - self.mot2[2]) <= 2:
                    # se nao houverem diferenças, sai do laço.
                    break
                else:
                    # caso ainda exista diferenças, significa que os motores ainda precisam se mover
                    # utiliza a funcao moverMotor para mover cada um dos motores ate a pos_escrita.
                    self.moverMotor(self.mot0[0], self.mot0[1])
                    self.moverMotor(self.mot1[0], self.mot1[1])
                    self.moverMotor(self.mot2[0], self.mot2[1])

    def ajustar(self, atual, min_ini, max_ini, min_final, max_final):
        """
        Converte o valor atual da sua atual faiixa de minimo e maximo, para um novo valor dentro correspondente a uma nova
        faixa de minimo e maximo
        """
        novo = (atual - min_ini) * (max_final - min_final) / (max_ini - min_ini) + min_final
        return novo

    def moverMotor(self, motor, angulo):

        mover = True
        if motor == 0:
            # realiza o mapeamento, de angulo para pulso PWM.
            pulso_pwm = self.ajustar(angulo, 0, 180, 150, 550)
            # Define os minimos e maximos de cada motor, para evitar travamento,
            # esses valores foram definidos manualmente com base em testes.
            if (pulso_pwm < 148) or (pulso_pwm > 560):
                mover = False

        if motor == 4:
            pulso_pwm = self.ajustar(angulo, 0, 90, 300, 545)
            if (pulso_pwm < 150) or (pulso_pwm > 580):
                mover = False

        if motor == 8:
            pulso_pwm = self.ajustar(angulo, 0, 160, 121, 480)
            if (pulso_pwm < 121) or (pulso_pwm > 480):
                mover = False

        if motor == 12:
            pulso_pwm = self.ajustar(angulo, 0, 60, 540, 350)
            if (pulso_pwm < 350) or (pulso_pwm > 540):
                mover = False
        if mover:
        # funcao da bibliteca Adafruit, que escreve o valor PWM em determinada porta.
            self.pca.channels[motor].duty_cycle = angulo
            sleep(0.03)
