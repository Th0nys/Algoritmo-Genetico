#para todo x P(x) E B(x)
import random
import numpy as np

prop = [[0,0],[0,1],[1,0],[1,1]]
pop = [[0 for i in range(4)] for j in range(8)]
apt = [0 for i in range(8)]

def gerarPop():
    for i in range(8):
        for j in range(4):
            pop[i][j] = bool(random.randint(0,1))
            
def mostra():
    print("--------------------------------")
    for i in range(7):
        print(pop[i])
    print("--------------------------------")
    
def mostraApt():
    print("++++++++++++++++++++++++++++++++")
    for i in range(7):
        print(apt[i])
    print("++++++++++++++++++++++++++++++++")
    
def avaliar():
    for i in range(8):
        for j in range(4):
            if (prop[j][0] * prop[j][1]) == pop[i][j]:
                apt[i] = apt[i] +1
           
def mutacao():
    escolha = int(len(prop) * 0.25)
    #print('\n')
    print(escolha)
    for i in range(8):
        for j in range(escolha):
            k = random.randint(0,3)
            pop[i][k] = not pop[i][k]
      
def selecao_roleta():
    total_acumulado = sum(apt)
    porcent = []
    frequencia_acumulada = []
    amostras = sorted(apt)
    for i in range(0, len(pop)):
        if i == 0:
            frequencia_acumulada.append(amostras[0])
        else:
            frequencia_acumulada.append(frequencia_acumulada[i-1] + amostras[i]) 
        porcent.append((frequencia_acumulada[i]/total_acumulado) * 100)
        
    print(f'avaliações = {apt}')
    print(f'frequencia_acumulada = {frequencia_acumulada}')
    print(f'{porcent}')



gerarPop()
mostra()
avaliar()
mostraApt()
mutacao()
mostra()
selecao_roleta()
