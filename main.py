from fuctions import *


gerarPop()
mostraPop()
mostraPopFil()
i = 0
while apt[3] != 4 and i < 20:
    avaliarPop()
    avaliarPopFil()
    mostraApt()
    ordenar(pop, apt)
    mutacao()
    avaliarPop()
    mostraPop()
    ordenar(pop, apt)
    mostraPop()
    avaliarPopFil()
    cruzamento(selecao_roleta())
    avaliarPopFil()
    ordenar(popFil, aptFil)
    cruzamento(selecao_roleta())
    avaliarPopFil()
    ordenar(popFil, aptFil)
    mostraPop()
    pop, apt = substituicao()
    mostraPop()
    mostraApt()
    ordenar(pop, apt)
    i = i + 1

print(f'{i} gerações para achar soluções')
