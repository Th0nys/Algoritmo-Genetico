from functions import *

gerarPop()
mostraPop()

i = 0
apto = True
while apto and i < 10:
    avaliarPop()
    avaliarPopFil()
    mostraApt()
    ordenar(pop, apt)
    mutacao()
    avaliarPop()
    mostraPop()
    ordenar(pop, apt)
    mostraApt()
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
    if apt[0] >= 4:
        apto = False
    i = i + 1
    
if not apto:
    print(f'{i} gerações para achar soluções')
    print(f'Solução encontrada: {pop[0]}')
    print(parse(pop[0]))
else:
    print("Não fora achada solução")
