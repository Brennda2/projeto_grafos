# Lista de Adjacência

def CriarGrafo():
    global direcionado, grafo
    grafo = {}
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
    if not grafo:
        print("O grafo está vazio.")
        return

    for vertice, vizinhos in grafo.items():
        print(f"{vertice} -> {vizinhos}")

def InserirVertice(vertice):
    if vertice not in grafo:
        grafo[vertice] = []
        print(f"O vértice {vertice} foi adicionado no grafo.")
        print(grafo)
    else:
        print(f"O vértice {vertice} já existe no grafo.")

def RemoverVertice(vertice):
    if vertice not in grafo:
        print("O vértice não existe no grafo.")
        return

    for vizinhos in grafo.values():
        while vertice in vizinhos:
            vizinhos.remove(vertice)

    del grafo[vertice]
    print(f"Vértice {vertice} removido.")
    print(grafo)

def InserirAresta(vertice1, vertice2):
    if vertice1 not in grafo:
        print("O vértice 1 não existe! Crie ele no menu!")
        return

    elif vertice2 not in grafo:
        print("O vértice 2 não existe! Crie ele no menu!")
        return

    else:
      if vertice2 not in grafo[vertice1]:
            grafo[vertice1].append(vertice2)

      if not direcionado and vertice1 not in grafo[vertice2]:
            grafo[vertice2].append(vertice1)

    print(grafo)

def RemoverAresta(vertice, vertice2):
   if vertice in grafo and vertice2 in grafo[vertice]:
        grafo[vertice].remove(vertice2)

        if not direcionado:
            if vertice2 in grafo and vertice in grafo[vertice2]:
                grafo[vertice2].remove(vertice)

        print(grafo)
   else:
        print("A aresta não existe no grafo.")

def CalcularGrau():
    for vertice in grafo:
        grau_saida = len(grafo[vertice])

        if direcionado:
            grau_entrada = 0

            for vizinhos in grafo.values():
                if vertice in vizinhos:
                    grau_entrada += 1

            print(f"Vértice {vertice}:\n Grau de saída = {grau_saida} \n Grau de entrada = {grau_entrada}")
        else:
            print(f"Grau do vértice {vertice}: {grau_saida}")

def VerificarArestaEntreVertices(vertice1,vertice2):
    if vertice1 in grafo and vertice2 in grafo[vertice1]:
      print(f"Existe uma aresta entre os vértices {vertice1} e {vertice2}")
      return True
    else:
      print(f"Não existe uma aresta entre os vértices {vertice1} e {vertice2}")
      return False

def ListarVizinhos(vertice):
    if vertice in grafo:
      print(f"Vizinhos de: {vertice} -> {grafo[vertice]}")
      return grafo[vertice]
    else:
      print(f"O vértice {vertice} não existe!")
      return None

def VerificarPercurso(vertice1, vertice2):
    if vertice1 not in grafo or vertice2 not in grafo:
        print("Um ou ambos os vértices não existem no grafo!")
        return False

    if vertice1 == vertice2:
        print(f"O vértice {vertice1} já é o destino.")
        return True

    fila = [vertice1]
    visitados = {vertice1}

    while fila:
        atual = fila.pop(0)

        if atual == vertice2:
            print(f"Existe um percurso entre {vertice1} e {vertice2}!")
            return True

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    print(f"Não existe um percurso entre {vertice1} e {vertice2}.")
    return False

# Inicialização
direcionado = False
grafo = {}
CriarGrafo()

while True:
    print("\n1 - Adicionar vértice")
    print("2 - Remover vértice")
    print("3 - Adicionar aresta")
    print("4 - Remover aresta")
    print("5 - Exibir o grau de cada vétice")
    print("6 - Verificar se existe uma aresta que vai de um vértice para o outro")
    print("7 - Listar todos os Vizinhos de um vértice")
    print("8 - Verificar se um determinado percurso é possível")
    print("9 - Exibir grafo")
    print("0 - Sair")

    op = int(input("Digite a opção deseja: "))

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