from typing import Optional
from cv2 import imread, imshow, rectangle, waitKey, VideoCapture
import dlib
import numpy
import os.path


class DetectorX:
    SVM = 'Z:/Python/projetos/RoboJogoVelha/visao/resources/svms/svmX.svm'
    COR_VERDE = (0, 255, 0)

    def __init__(self, fonteImagem: str, svm: str):
        """
        :param fonteImagem: fonte da imagem a ser analizada, pode ser um diretorio de arquivo
        ou a String 'camera:numerodispositivo', por padrao o numero é 0
        :param svm: diretorio do arquivo .svm
        """
        self.fonteImagem = fonteImagem
        if svm is not None:
            self.svm = dlib.simple_object_detector(svm)
        else:
            self.svm = dlib.simple_object_detector(DetectorX.SVM)

        self.objs = []
        self.deteccoes = dict
        self.detectado = False

    def detectar(self):
        imagem = self.capturar_imagem()
        deteccoes = self.svm(imagem)
        if len(deteccoes) > 0:
            self.detectado = True
            for obj in deteccoes:
                objeto = [obj.left(), obj.right(), obj.top(), obj.bottom()]
                area = (obj.right() - obj.left()) * (obj.bottom() - obj.top())
                objeto.append(area)
                self.objs.append(objeto)
        return self.detectado

    def desenhar(self):
        if self.detectado is True and len(self.objs) > 0:
            for obj in self.objs:
                if obj[4] > 40000:
                    esq = obj[0]
                    drt = obj[1]
                    top = obj[2]
                    bot = obj[3]
                    rectangle(self.fonteImagem, (esq, top), (drt, bot), DetectorX.COR_VERDE, 2)
        return self.fonteImagem

    def exibir(self):
        imshow('Resultado', self.fonteImagem)
        waitKey(0)

    def capturar_imagem(self) -> numpy.ndarray:
        try:
            if os.path.exists(self.fonteImagem):
                return imread(self.fonteImagem)
            if self.fonteImagem.lower().count("camera") > 0:
                num_cam = 0
                if self.fonteImagem.count(':') > 0:
                    num_cam = int(self.fonteImagem.split(':')[1])
                cam = VideoCapture(num_cam)
                status, imagem = cam.read()
                if status is True:
                    return imagem
                raise Exception('Nao foi possivel obter a imagem, o metodo read() retornou status False')
        except Exception as e:
            print('Erro ao obter imagem: ', e)
