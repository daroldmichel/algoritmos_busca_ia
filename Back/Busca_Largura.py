from collections import deque
from Cidade import Adjacente


class Busca_Largura:

    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fila = deque([Adjacente(inicio, 0)])
        self.qtdtestes = 0

    def buscar(self):
        if len(self.fila) > 0:
            #Pega primeira cidade da Fila
            primeiro = list(self.fila)[0].cidade

            #Incrementa contador de testes
            self.qtdtestes += 1

            #Se o primeiro da fila é a cidade objetivo, chegou ao destino
            if primeiro == self.objetivo:
                self.objetivo = primeiro
                return self
            else:
                #Remove o primeiro item da Fila
                self.fila.popleft()
                #Se não é a cidade objetivo, precisa incluir os ajdacentes dela ao final da fila

                for a in primeiro.adjacentes:
                    #Se já testou uma vez não testa mais
                    if a.cidade.visitado == False:
                        #Marca a cidade como visitada, para não incluir ela na novamente
                        a.cidade.visitado = True
                        a.cidade.paiAdjacente = Adjacente(primeiro, a.distancia)
                        #Inclui adjacente na fila
                        self.fila.append(a)
                        #Inicia a busca
                return Busca_Largura.buscar(self)
