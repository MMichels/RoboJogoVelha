from minmaxtoe import MinMaxToe

jogo = MinMaxToe('X')
while not jogo.fim_jogo():
    mov = int(input('Digite a posição do movimento: ')) - 1
    mov = jogo.posicoes[mov]
    if mov not in jogo.esp_livres():
        print('Movimento invalido, posição ja ocupada.')
        continue
    jogo.realiza_mov(MinMaxToe.JOGADOR, mov)
    jogo.mv_computador()
    jogo.exibir()

print('Vencedor = {}'.format(jogo.obter_vencedor()))
