from detector import DetectorX
from cv2 import imread
import os, glob


for foto in glob.glob(os.path.join('../resources/imagens/teste', '*.jpg')):
    detector = DetectorX(foto, '../resources/svms/svmX.svm')
    detector.detectar()
    detector.desenhar()
    detector.exibir()
