#para todo x P(x) E B(x)
import random

prop = [[0,0],[0,1],[1,0],[1,1]]
pop = [[0 for i in range(4)] for j in range(16)]
popFil = [[0 for i in range(4)] for j in range(8)]
apt = [0 for i in range(16)]
aptFil = [0 for i in range(8)]

def gerarPop():
    for i in range(len(pop)):
        for j in range(len(pop[i])):
            pop[i][j] = bool(random.randint(0,1))
            
def mostraPop():
    print("--------------------------------")
    for i in range(len(pop)):
        print(pop[i])
    print("--------------------------------")

def mostraPopFil():
    print("--------------------------------")
    for i in range(len(popFil)):
        print(popFil[i])
    print("--------------------------------")
    
def mostraApt():
    print("++++++++++++APTIDÃO+++++++++++++")
    for i in range(len(apt)):
        print(apt[i])
    print("++++++++++++++++++++++++++++++++")
    
def avaliarPop():
    print("\nAvaliando populacao...\n")
    for i in range(len(pop)):
        apt[i] = 0
        for j in range(len(prop)):
            if (prop[j][0] * prop[j][1]) == pop[i][j]:
                apt[i] = apt[i] + 1

def avaliarPopFil():
    print("\nAvaliando descendentes...\n")
    for i in range(len(popFil)):
        aptFil[i] = 0
        for j in range(len(prop)):
            if (prop[j][0] * prop[j][1]) == popFil[i][j]:
                aptFil[i] = aptFil[i] + 1
           
def mutacao():
    print("\nMutando populacao...\n")
    escolha = int(len(prop) * 0.25)
    print(escolha)
    for i in range(len(pop)):
        k1 = random.randint(0,3)
        print(f'{i} e {k1}')
        pop[i][k1] = not pop[i][k1]
      
def selecao_roleta():
    print("\nSelecionando...\n")
    melhores = []
    total_acumulado = sum(apt)
    porcent = []
    frequencia_acumulada = []
    amostras = apt
    for i in range(0, len(pop)):
        if i == 0:
            frequencia_acumulada.append(amostras[0])
        else:
            frequencia_acumulada.append(frequencia_acumulada[i-1] + amostras[i]) 
        porcent.append((frequencia_acumulada[i]/total_acumulado) * 100)

    check = False
    while check is False:
        ind1 = random.uniform(0,100)
        ind2 = random.uniform(0,100)

        quartil = 0.0
        indice1 = 0
        indice2 = 0

        for i in range(len(porcent)):
            if ind1 > quartil and ind1 <= porcent[i]:
                melhores.append(i)
                melhores.append(pop[i])
                indice1 = i
            if ind2 > quartil and ind2 <= porcent[i]:
                melhores.append(i)
                melhores.append(pop[i])
                indice1 = i
            quartil = porcent[i]
        
        if indice1 != indice2:
            check = True
        else:
            melhores.clear()

    print(f'avaliações = {apt}')
    print(f'frequencia_acumulada = {frequencia_acumulada}')
    print(f'{porcent}')
    print(f'selecionados = {melhores}')

    return melhores

def cruzamento(pais = []):
    print("\nEfetuando cruzamento...\n")
    popFil[0][0] = pais[1][0]
    popFil[0][1] = pais[3][1]
    popFil[0][2] = pais[1][2]
    popFil[0][3] = pais[3][3]
    popFil[1][0] = pais[3][0]
    popFil[1][1] = pais[1][1]
    popFil[1][2] = pais[3][2]
    popFil[1][3] = pais[1][3]

    #popFil[2][0] = pais[2][0]
    #popFil[2][1] = pais[2][1]
    #popFil[2][2] = pais[3][2]
    #popFil[2][3] = pais[3][3]
    #popFil[3][0] = pais[3][0]
    #popFil[3][1] = pais[3][1]
    #popFil[3][2] = pais[2][2]
    #popFil[3][3] = pais[2][3]

def substituicao():
    print("\nSubstituindo populacao...\n")
    novaPop = []
    novaApt = []
    i = 0
    j = 0
    for i in range(len(pop)):
        for j in range(len(popFil)):
            if apt[i] > aptFil[j]:
                novaPop.append(pop[i])
                novaApt.append(apt[i])
                i+1
                break
            else:
                novaPop.append(popFil[j])
                novaApt.append(aptFil[j])
                j+1
                break

    print(f'{len(novaPop)}, {len(novaApt)}')
    
    return novaPop, novaApt

def ordenar(populacao = [], adapt = []):
    print("\nOrdenando populacao...\n")
    for i in range(len(populacao)):
        for j in range(i+1, len(populacao)):
            if adapt[i] < adapt[j]:
                temp = populacao[i]
                populacao[i] = populacao[j]
                populacao[j] = temp
                temp = adapt[i]
                adapt[i] = adapt[j]
                adapt[j] = temp


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