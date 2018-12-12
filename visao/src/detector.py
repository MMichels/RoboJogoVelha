from typing import Optional

from cv2 import imread, imshow, rectangle, waitKey
import dlib
import os.path


class DetectorX:
    SVM = '../resources/svms/svmX.svm'
    COR_VERDE = (0, 255, 0)

    def __init__(self, img, svm: str):
        """
        :param img: Imagem a ser analizada
        :param svm: diretorio do arquivo .svm
        """
        self.img = imread(img)
        if svm is not None:
            self.svm = dlib.simple_object_detector(svm)
        else:
            self.svm = dlib.simple_object_detector(DetectorX.SVM)

        self.objs = []
        self.deteccoes = dict
        self.detectado = False

    def detectar(self):
        deteccoes = self.svm(self.img)
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
                    dir = obj[1]
                    top = obj[2]
                    bot = obj[3]
                    rectangle(self.img, (esq, top), (dir, bot), DetectorX.COR_VERDE, 2)
        return self.img

    def exibir(self):
        imshow('Resultado', self.img)
        waitKey(0)
