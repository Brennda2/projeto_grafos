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

def InserirVertice(vertice):
    if vertice not in vertices:
        vertices.append(vertice)
        for linha in matriz:
            linha.append(0)
        nova_linha = [0] * len(vertices)
        matriz.append(nova_linha)
        print(f"Vértice {vertice} adicionado!")
    else:
        print(f"O vértice {vertice} já existe no grafo.")
    ExibirGrafo()

def InserirAresta(vertice1, vertice2):
    if vertice1 not in vertices:
        print("O vértice 1 não existe! Crie ele no menu!")
        return
    if vertice2 not in vertices:
        print("O vértice 2 não existe! Crie ele no menu!")
        return

    i = vertices.index(vertice1)
    j = vertices.index(vertice2)

    matriz[i][j] = 1

    if not direcionado:
        matriz[j][i] = 1

    ExibirGrafo()

def RemoverVertice(vertice):
    if vertice not in vertices:
        print("O vértice não existe no grafo.")
        return

    i = vertices.index(vertice)
    matriz.pop(i)
    for linha in matriz:
        linha.pop(i)
    vertices.remove(vertice)

    print(f"Vértice {vertice} removido com sucesso!")
    ExibirGrafo()

def RemoverAresta(vertice1, vertice2):
    if vertice1 in vertices and vertice2 in vertices:
        i = vertices.index(vertice1)
        j = vertices.index(vertice2)

        matriz[i][j] = 0
        if not direcionado:
            matriz[j][i] = 0

        print(f"Aresta entre {vertice1} e {vertice2} removida!")
        ExibirGrafo()
    else:
        print("Um ou ambos os vértices não existem no grafo.")

def CalcularGrau():
    for i in range(len(vertices)):
        vertice = vertices[i]
        saida = 0
        for j in range(len(vertices)):
            saida += matriz[i][j]

        entrada = 0
        for linha in range(len(vertices)):
            entrada += matriz[linha][i]

        if direcionado:
            print(f"Vértice {vertice}:\n Grau de saída = {saida} \n Grau de entrada = {entrada} \n Grau total = {saida + entrada}")
        else:
            print(f"Grau do vértice {vertice}: {saida}")

def VerificarArestaEntreVertices(vertice1, vertice2):
    if vertice1 in vertices and vertice2 in vertices:
        i = vertices.index(vertice1)
        j = vertices.index(vertice2)
        if matriz[i][j] == 1:
            print(f"Existe uma aresta entre os vértices {vertice1} e {vertice2}")
            return True
    print(f"Não existe uma aresta entre os vértices {vertice1} e {vertice2}")
    return False

def ListarVizinhos(vertice):
    if vertice in vertices:
        i = vertices.index(vertice)
        lista_vizinhos = []
        for j in range(len(vertices)):
            if matriz[i][j] == 1:
                lista_vizinhos.append(vertices[j])
        print(f"Vizinhos de {vertice} -> {lista_vizinhos}")
        return lista_vizinhos
    else:
        print(f"O vértice {vertice} não existe!")
        return None

def VerificarPercurso(vertice1, vertice2):
    if vertice1 not in vertices or vertice2 not in vertices:
        print("Um ou ambos os vértices não existem no grafo!")
        return False

    if vertice1 == vertice2:
        print(f"O vértice {vertice1} já é o destino.")
        return True

    i_origem = vertices.index(vertice1)

    fila = [i_origem]
    visitados = {i_origem}

    while fila:
        atual_idx = fila.pop(0)

        if vertices[atual_idx] == vertice2:
            print(f"Existe um percurso entre {vertice1} e {vertice2}!")
            return True

        for j in range(len(vertices)):
            if matriz[atual_idx][j] == 1 and j not in visitados:
                visitados.add(j)
                fila.append(j)

    print(f"Não existe um percurso entre {vertice1} e {vertice2}.")
    return False

def ExibirGrafo():
    if not vertices:
        print("Grafo vazio.")
        return
    print("\n--- Matriz de Adjacência ---")
    print("\t" + "\t".join(str(v) for v in vertices))
    for i in range(len(vertices)):
        vertice = vertices[i]
        linha_str = "\t".join(str(val) for val in matriz[i])
        print(f"{vertice}\t{linha_str}")
    print("-" * 30)

# Inicialização das variáveis globais
direcionado = False
matriz = []
vertices = []

CriarGrafo()

while True:
    print("\n1 - Adicionar vértice")
    print("2 - Remover vértice")
    print("3 - Adicionar aresta")
    print("4 - Remover aresta")
    print("5 - Exibir o grau de cada vértice")
    print("6 - Verificar se existe uma aresta que vai de um vértice para o outro")
    print("7 - Listar todos os Vizinhos de um vértice")
    print("8 - Verificar se um determinado percurso é possível")
    print("9 - Exibir Matriz")
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
            print("\n --- Verifica se a aresta vai de um vértice para outro ---")
            vertice1 = input("Digite o vértice origem: ")
            vertice2 = input("Digite o vértice destino: ")
            VerificarArestaEntreVertices(vertice1, vertice2)
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