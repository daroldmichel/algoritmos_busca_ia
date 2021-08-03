class Adjacente:
    def __init__(self, cidade, distancia):
        self.cidade = cidade
        self.distancia = distancia


class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.adjacentes = []
        self.visitado = False
        self.paiAdjacente = None
        
    def addCidadeAdjacente(self, adjacente):
        self.adjacentes.append(adjacente)