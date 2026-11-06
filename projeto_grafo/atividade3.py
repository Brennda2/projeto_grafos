# Lista de Arestas

vertices = []
grafo = []

def CriarGrafo():
    global direcionado
    while True:
        tipo = input("O grafo é direcionado? (s/n): ").lower()
        if tipo == "s":
            direcionado = True
            return
        elif tipo == "n":
            direcionado = False
            return
        else:
            print("Opção inválida!")

def ExibirGrafo():
    if vertices:
        print("\n--- Lista de Arestas ---")
        print(f"Vértices: {vertices}")
        print("Arestas:")

        for aresta in grafo:
            print(f"{aresta[0]} -> {aresta[1]}")
    else:
        print("O grafo está vazio.")

def InserirVertice(vertice):
    if vertice not in vertices:
        vertices.append(vertice)
        print(f"Vértice {vertice} adicionado!")
    else:
        print(f"O vértice {vertice} já existe no grafo.")
    ExibirGrafo()

def RemoverVertice(vertice):
    if vertice in vertices:
        for aresta in grafo[:]:
            if vertice in aresta:
                grafo.remove(aresta)

        vertices.remove(vertice)
        print(f"Vértice {vertice} removido!")
        ExibirGrafo()
    else:
        print(f"O vértice {vertice} não existe no grafo.")

def InserirAresta(vertice1,vertice2):
    if vertice1 not in vertices:
        print("O vértice 1 não existe! Crie ele no menu!")
        return
    if vertice2 not in vertices:
        print("O vértice 2 não existe! Crie ele no menu!")
        return
    grafo.append([vertice1,vertice2])
    
    if not direcionado:
        grafo.append([vertice2,vertice1])

    ExibirGrafo()

def RemoverAresta(vertice1, vertice2):
    if vertice1 in vertices and vertice2 in vertices:
        if [vertice1, vertice2] in grafo:
            grafo.remove([vertice1, vertice2])

            if not direcionado:
                if [vertice2, vertice1] in grafo:
                    grafo.remove([vertice2, vertice1])

            print("Aresta removida!")
            ExibirGrafo()
        else:
            print("Essa aresta não existe no grafo.")
    else:
        print("Um ou ambos os vértices não existem no grafo.")

def CalcularGrau():
    if vertices:
        for vertice in vertices:
            saida = 0
            entrada = 0
            for i in grafo:
                    if i[0] == vertice:
                        saida += 1
                    if i[1] == vertice:
                        entrada +=1
            if direcionado:
                print(f"Vértice {vertice}:\n Grau de saída = {saida} \n Grau de entrada = {entrada} \n Grau Total = {entrada + saida}")
            else:
                print(f"Grau do vértice {vertice}: {saida}")
    else:
        print(f"Não existe grafo.")

def ExisteAresta(vertice1, vertice2):
    if [vertice1, vertice2] in grafo:
        print("Existe uma aresta entre os vértices!")

    else:
        print("Não existe uma aresta entre os vértices.")

def ListarVizinhos(vertice):
    if vertice not in vertices:
        print(f"O vértice {vertice} não existe no grafo.")
        return

    vizinhos = []

    for aresta in grafo:
        if aresta[0] == vertice:
            vizinhos.append(aresta[1])

    if vizinhos:
        print(f"Vizinhos do vértice {vertice}: {vizinhos}")
    else:
        print(f"O vértice {vertice} não possui vizinhos.")



def VerificarPercurso(vertice1, vertice2):
    if vertice1 not in vertices:
        print(f"O vértice {vertice1} não existe no grafo.")
        return

    if vertice2 not in vertices:
        print(f"O vértice {vertice2} não existe no grafo.")
        return

    visitados = []
    fila = [vertice1]

    while fila:
        atual = fila.pop(0)

        if atual == vertice2:
            print(f"Existe percurso de {vertice1} até {vertice2}!")
            return

        if atual not in visitados:
            visitados.append(atual)

            for aresta in grafo:
                if aresta[0] == atual and aresta[1] not in visitados:
                    fila.append(aresta[1])

    print(f"Não existe percurso de {vertice1} até {vertice2}.")


CriarGrafo()


while True:
    print("\n1 - Adicionar vértice")
    print("2 - Remover vértice")
    print("3 - Adicionar aresta")
    print("4 - Remover aresta")
    print("5 - Exibir o grau de cada vértice")
    print("6 - Existe Aresta que vai de um vértice para outro")
    print("7 - Listar todos os Vizinhos de um vértice")
    print("8 - Verificar se um determinado percurso é possível")
    print("9 - Exibir Lista de Arestas")
    print("0 - Sair")

    op = int(input("Digite a opção desejada: "))

    match op:
        case 1:
            print("\n --- Adicionar vértice ---")
            vertice = input("Digite o vértice que deseja: ")
            InserirVertice(vertice)
        case 2:
            print("\n --- Remover vértice ---")
            vertice = input("Digite o vértice que deseja: ")
            RemoverVertice(vertice)
        case 3:
            print("\n --- Adicionar Aresta ---")
            vertice = input("Digite o vértice origem: ")
            aresta = input("Digite o vértice destino (aresta): ")
            InserirAresta(vertice, aresta)
        case 4:
            print("\n --- Remover Aresta ---")
            vertice = input("Digite o vértice origem: ")
            aresta = input("Digite o vértice destino (aresta): ")
            RemoverAresta(vertice, aresta)
        case 5:
            print("\n --- Grau de cada Vértice ---")
            CalcularGrau()
        case 6:
            print("\n --- Existe Aresta ---")
            vertice1 = input("Digite o vértice de origem: ")
            vertice2 = input("Digite o vértice de destino: ")
            ExisteAresta(vertice1, vertice2)
        case 7:
            print("\n --- Vizinho de cada Vértice ---")
            vertice = input("Digite o vértice que deseja: ")
            ListarVizinhos(vertice)
        case 8:
            print("\n --- Verificar Percurso ---")
            vertice1 = input("Digite o vértice de origem: ")
            vertice2 = input("Digite o vértice de destino: ")
            VerificarPercurso(vertice1, vertice2)
        case 9:
            ExibirGrafo()
        case 0:
            print("Programa Encerrado!")
            break
        case _:
            print("Opção inválida")