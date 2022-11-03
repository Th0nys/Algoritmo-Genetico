import random
#entrada
#   A   B|  S
#   F   F|  F
#   F   V|  V
#   V   F|  V
#   V   V|  V

#Simbolos lógicos:
#     or == 2
#     and == 3
#     implica == 4
#     bi-implica == 5
#     xor = 6

#Cromossomo
#[ , , , , , , , ]
#[~,A,OU, ,B,-->, ,A]
#[ ,B,E, ,A,<-->,~,B]

# Tabela Verdade
prop = [[False, False, True, True],
        [False, True, False, True],
        [False, True, True, True ]
       ]
pop = [[0 for i in range(8)] for j in range(6)]
popFil = [[0 for i in range(8)] for j in range(4)]
apt = [0 for i in range(6)]
aptFil = [0 for i in range(4)]

def gerarPop():
    for i in range(len(pop)):
        next = 0
        for j in range(len(pop[i])):
            if next == 0:
                pop[i][j] = bool(random.randint(0,1))
                next = 1
            elif next == 1:
                letras = ['a','b']
                pop[i][j] = letras[random.randint(0,1)]
                next = 2
            else:
                pop[i][j] = random.randint(2,6)
                next = 0

def gerarPopFil():
    for i in range(len(popFil)):
        next = 0
        for j in range(len(popFil[i])):
            if next == 0:
                popFil[i][j] = bool(random.randint(0,1))
                next = 1
            elif next == 1:
                letras = ['a','b']
                popFil[i][j] = letras[random.randint(0,1)]
                next = 2
            else:
                popFil[i][j] = random.randint(2,6)
                next = 0
            
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
        k = 0
        while k + 5 <= len(pop[i]): 
            for j in range(len(prop[2])):
                a = None
                b = None
                if pop[i][k+1] == 'a':
                    a = prop[0][j]
                else:
                    a = prop[1][j]
                if pop[i][k+3] == 'a':
                    b = prop[0][j]
                else:
                    b = prop[1][j]

                if pop[i][k] != False:
                    a = not a
                if pop[i][k+3] != False:
                    b = not b

                if pop[i][k+2] == 2:
                    if (a or b) == prop[2][j]:
                        apt[i] = apt[i] + 1
                elif pop[i][k+2] == 3:
                    if (a and b) == prop[2][j]:
                        apt[i] = apt[i] + 1
                elif pop[i][k+2] == 4:
                    if (a <= b) == prop[2][j]:
                        apt[i] = apt[i] + 1
                elif pop[i][k+2] == 5:
                    if ((a <= b) and (b <= a)) == prop[2][j]:
                        apt[i] = apt[i] + 1
                elif pop[i][k+2] == 6:
                    if (a ^ b) == prop[2][j]:
                        apt[i] = apt[i] + 1
            k = k + 3
    print("--------------------------------")

def avaliarPopFil():
    print("\nAvaliando descendentes...\n")
    for i in range(len(popFil)):
        aptFil[i] = 0
        k = 0
        while k + 5 <= len(popFil[i]): 
            for j in range(len(prop[2])):
                a = None
                b = None
                if popFil[i][k+1] == 'a':
                    a = prop[0][j]
                else:
                    a = prop[1][j]
                if popFil[i][k+3] == 'a':
                    b = prop[0][j]
                else:
                    b = prop[1][j]

                if popFil[i][k] != False:
                    a = not a
                if popFil[i][k+3] != False:
                    b = not b

                if popFil[i][k+2] == 2:
                    if (a or b) == prop[2][j]:
                        aptFil[i] = aptFil[i] + 1
                elif popFil[i][k+2] == 3:
                    if (a and b) == prop[2][j]:
                        aptFil[i] = aptFil[i] + 1
                elif popFil[i][k+2] == 4:
                    if (a <= b) == prop[2][j]:
                        aptFil[i] = aptFil[i] + 1
                elif popFil[i][k+2] == 5:
                    if ((a <= b) and (b <= a)) == prop[2][j]:
                        aptFil[i] = aptFil[i] + 1
                elif popFil[i][k+2] == 6:
                    if (a ^ b) == prop[2][j]:
                        aptFil[i] = aptFil[i] + 1
            k = k + 3
    print("--------------------------------")
           
def mutacao():
    print("\nMutando populacao...\n")
    for i in range(len(pop)):
        k1 = random.randint(0,len(pop[1])-1)
        print(f'{i} e {k1}')
        if pop[i][k1] == True:
            pop[i][k1] = not pop[i][k1]
        elif pop[i][k1] == False:
            pop[i][k1] = not pop[i][k1]
        elif pop[i][k1] == 'a':
            pop[i][k1] = 'b'
        elif pop[i][k1] == 'b':
                pop[i][k1] = 'a'
        else:
            k2 = random.randint(2,6)
            print(f'{k2}')
            while k2 == pop[i][k1]:
                k2 = random.randint(2,6)
                print(f'{k2}')
            pop[i][k1] = k2
    print("--------------------------------")
      
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
                print(i)
                indice1 = i
            if ind2 > quartil and ind2 <= porcent[i]:
                melhores.append(i)
                melhores.append(pop[i])
                print(i)
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
    print("--------------------------------")
    return melhores

def cruzamento(pais = []):
    print("\nEfetuando cruzamento...\n")
    e = random.randint(0,1)
    if e == 0:          #Ponto de corte no indice 3
        popFil[0][0] = pais[1][0]
        popFil[0][1] = pais[1][1]
        popFil[0][2] = pais[1][2]
        popFil[0][3] = pais[3][3]
        popFil[0][4] = pais[3][4]
        popFil[0][5] = pais[3][5]
        popFil[0][6] = pais[3][6]
        popFil[0][7] = pais[3][7]

        popFil[1][0] = pais[3][0]
        popFil[1][1] = pais[3][1]
        popFil[1][2] = pais[3][2]
        popFil[1][3] = pais[1][3]
        popFil[1][4] = pais[1][4]
        popFil[1][5] = pais[1][5]
        popFil[1][6] = pais[1][6]
        popFil[1][7] = pais[1][7]
    else:          #Ponto de corte no indice 5
        popFil[0][0] = pais[1][0]
        popFil[0][1] = pais[1][1]
        popFil[0][2] = pais[1][2]
        popFil[0][3] = pais[1][3]
        popFil[0][4] = pais[1][4]
        popFil[0][5] = pais[3][5]
        popFil[0][6] = pais[3][6]
        popFil[0][7] = pais[3][7]

        popFil[1][0] = pais[3][0]
        popFil[1][1] = pais[3][1]
        popFil[1][2] = pais[3][2]
        popFil[1][3] = pais[3][3]
        popFil[1][4] = pais[3][4]
        popFil[1][5] = pais[1][5]
        popFil[1][6] = pais[1][6]
        popFil[1][7] = pais[1][7]
    print("--------------------------------")

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
    print("--------------------------------")
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
    print("--------------------------------")

def parse(solucao = []):
    resultado = "A solução é: "
    for i in range(len(solucao)):
        if solucao[i] == False:
            resultado = resultado + ""
        if solucao[i] == True:
            resultado = resultado + " ~"
        elif solucao[i] == 'a':
            resultado = resultado + "A"
        elif solucao[i] == 'b':
            resultado = resultado + "B"
        elif solucao[i] == 2:
            resultado = resultado + " OU "
        elif solucao[i] == 3:
            resultado = resultado + " E "
        elif solucao[i] == 4:
            resultado = resultado + " --> "
        elif solucao[i] == 5:
            resultado = resultado + " <--> "
        elif solucao[i] == 6:
            resultado = resultado + " XOR "
    
    return resultado
