from collections import deque
from Cidade import Adjacente


class Busca_Profundidade:

    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.pilha = deque([Adjacente(inicio, 0)])
        self.qtdtestes = 0

    def buscar(self):
        if len(self.pilha) > 0:
            #Pega cidade dopo da pilha
            topo = list(self.pilha)[len(self.pilha) - 1].cidade
            #Seta a cidade como visitada (Se já testou uma vez ela, não precisa testar mais)
            topo.visitado = True
            #Incrementa contador de testes
            self.qtdtestes += 1

            #Se o topo da pilha é a cidade objetivo, chegou ao destino
            if topo == self.objetivo:
                return self
            else:
                #Se não é a cidade objetivo, precisa incluir os ajdacentes dela ao topo da pilha e já ir testando

                for a in topo.adjacentes:
                    #Se já testou uma vez não testa mais
                    if a.cidade.visitado == False:
                        #Inclui adjacente na pilha
                        self.pilha.append(a)
                        #Inicia a busca agora com o Adjacente no topo da pilha
                        return Busca_Profundidade.buscar(self)
                if topo.visitado:
                    #Se o topo já foi visitado, não tem mais filhos a serem acrescentados a pilha e não é ele o objetivo
                    #Remove ele do topo e segue realizando a busca (agora com o anterior no topo)
                    self.pilha.pop()
                    return Busca_Profundidade.buscar(self)
