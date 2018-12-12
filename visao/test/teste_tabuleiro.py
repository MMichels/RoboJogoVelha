import cv2

imagem = cv2.imread('../resources/imagens/teste_tabuleiro/tabuleiro.jpg')
largura, altura = imagem.shape[:2]
largura_div = largura / 3
altura_div = altura / 3
lista_partes = []
for x in range(3):
    x_parte = largura_div * x
    for y in range(3):
        y_parte = altura_div * y
        lista_partes.append([x_parte, y_parte])

for c in range(9):
    x_ini = int(lista_partes[c][0])
    x_end = int(x_ini + largura_div)
    y_ini = int(lista_partes[c][1])
    y_end = int(y_ini + largura_div)
    parte = imagem[x_ini:x_end, y_ini:y_end]

    cv2.imshow('Parte {}'.format(c), parte)
    cv2.imwrite('../resources/imagens/teste_tabuleiro/parte_{}.jpg'.format(c), parte)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
