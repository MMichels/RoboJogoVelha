from detector import DetectorX
import cv2

cam = cv2.VideoCapture(0)
visao = DetectorX('camera:0', None)
while True:
    visao.detectar()
    visao.desenhar()
    cv2.imshow('Camera', visao.capturar_imagem())
    if visao.detectado:
        print('detectado')
        input()
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

# When everything done, release the capture
cam.release()
exit(0)
