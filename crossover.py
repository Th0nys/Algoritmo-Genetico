#para todo x P(x) E B(x)
import random
import numpy as np

prop = [[0,0],[0,1],[1,0],[1,1]]
pop = [[0 for i in range(4)] for j in range(8)]
popFil = [[0 for i in range(4)] for j in range(8)]
apt = [0 for i in range(8)]
aptFil = [0 for i in range(8)]

def gerarPop():
    for i in range(8):
        for j in range(4):
            pop[i][j] = bool(random.randint(0,1))
            
def mostraPop():
    print("--------------------------------")
    for i in range(7):
        print(pop[i])
    print("--------------------------------")

def mostraPopFil():
    print("--------------------------------")
    for i in range(7):
        print(popFil[i])
    print("--------------------------------")
    
def mostraApt():
    print("++++++++++++++++++++++++++++++++")
    for i in range(7):
        print(apt[i])
    print("++++++++++++++++++++++++++++++++")
    
def avaliarPop():
    for i in range(8):
        for j in range(4):
            if (prop[j][0] * prop[j][1]) == pop[i][j]:
                apt[i] = apt[i] + 1

def avaliarPopFil():
    for i in range(8):
        for j in range(4):
            if (prop[j][0] * prop[j][1]) == popFil[i][j]:
                aptFil[i] = aptFil[i] + 1
           
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

def cruzamento():
    popFil[0][0] = pop[0][0]
    popFil[0][1] = pop[0][1]
    popFil[0][2] = pop[1][2]
    popFil[0][3] = pop[1][3]
    popFil[1][0] = pop[1][0]
    popFil[1][1] = pop[1][1]
    popFil[1][2] = pop[0][2]
    popFil[1][3] = pop[0][3]

    popFil[2][0] = pop[2][0]
    popFil[2][1] = pop[2][1]
    popFil[2][2] = pop[3][2]
    popFil[2][3] = pop[3][3]
    popFil[3][0] = pop[3][0]
    popFil[3][1] = pop[3][1]
    popFil[3][2] = pop[2][2]
    popFil[3][3] = pop[2][3]

def substituicao():
    pass

gerarPop()
mostraPop()
mostraPopFil()
avaliarPop()
avaliarPopFil()
mostraApt()
mutacao()
mostraPop()
selecao_roleta()
