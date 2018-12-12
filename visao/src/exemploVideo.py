import detector
import cv2

cam = cv2.VideoCapture(0)
detector = detector.DetectorX(None, None)
while(True):
    ret, imagem = cam.read()
    detector.img = imagem
    detector.detectar()
    detector.desenhar()
    cv2.imshow('Camera', detector.img)
    if detector.detectado:
        print('detectado')
        input()
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

# When everything done, release the capture
cam.release()
exit(0)
