import Mapa
from flask import Flask, jsonify
from collections import deque
from Cidade import Adjacente
from Busca_Profundidade import Busca_Profundidade
from Busca_Largura import Busca_Largura

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def print_cidades(cidades):
    aux = 1
    text = ""
    for cidade in cidades:
        if aux in (7, 13, 19, 24):
            text += "\n"
        text += "(" + format(aux) + ") " + cidade.nome + " | "
        aux += 1
    print(text)


def busca_origem(cidades):
    print('Com base na lista de Cidades abaixo, selecione o (Número) correspondente a Origem.')

    print_cidades(cidades)
    origem = int(input('Informe a Origem desejada: ')) - 1
    if 0 <= origem <= 26:
        print('Origem Selecionada: {}'.format(cidades[origem].nome))
        return origem
    else:
        print('Dados Incorretos!')
        return busca_origem(cidades)


def busca_destino(cidades):
    print('Com base na lista de Cidades abaixo, selecione o (Número) correspondente ao seu Destino.')

    print_cidades(cidades)
    origem = int(input('Informe o Destino desejada: ')) - 1
    if 0 <= origem <= 26:
        print('Destino Selecionado: {}'.format(cidades[origem].nome))
        return origem
    else:
        print('Dados Incorretos!')
        return busca_destino(cidades)


@app.route("/busca_profundidade/<int:id_origem>/<int:id_destino>", methods=['GET'])
def busca_profundidade(id_origem, id_destino):
    cidades = Mapa.lista_cidades()
    busca = Busca_Profundidade(cidades[id_origem], cidades[id_destino])

    print('Origem: {}'.format(cidades[id_origem].nome), '| Destino: {}'.format(cidades[id_destino].nome))
    busca.buscar()
    caminho = list(busca.pilha)

    rota = list()
    aux = 0
    dist = 0
    print('------------------------------------------------------------------------')
    for ca in caminho:
        aux += 1
        dist += ca.distancia
        if aux == 1:
            print('Embarque: {}'.format(ca.cidade.nome))
        else:
            item_rota = dict(
                {
                    "ordem": aux - 1,
                    "cidade": ca.cidade.nome,
                    "distancia": ca.distancia
                }
            )
            rota.append(item_rota)
            print('Destino {}:'.format(aux - 1), ca.cidade.nome, '| Distancia: {}'.format(ca.distancia))
        if aux == len(caminho):
            print('Distancia Total: {}'.format(dist), 'Quantidade de testes: {}'.format(busca.qtdtestes))
    print('------------------------------------------------------------------------')
    viagem = dict({
        "origem": cidades[id_origem].nome,
        "destino": cidades[id_destino].nome,
        "distancia_total": dist,
        "qtd_testes": busca.qtdtestes,
        "rota": rota
    })
    return jsonify(dict(viagem))


@app.route("/busca_largura/<int:id_origem>/<int:id_destino>", methods=['GET'])
def busca_largura(id_origem, id_destino):
    cidades = Mapa.lista_cidades()
    busca = Busca_Largura(cidades[id_origem], cidades[id_destino])

    print('Origem: {}'.format(cidades[id_origem].nome), '| Destino: {}'.format(cidades[id_destino].nome))
    busca.buscar()

    pai = busca.objetivo.paiAdjacente
    rota = list()
    dist = 0
    if (pai):
        ordem = deque([Adjacente(busca.objetivo, pai.distancia)])
        while (pai):
            eu = pai.cidade
            pai = pai.cidade.paiAdjacente
            if (pai):
                ordem.append(Adjacente(eu, pai.distancia))
            else:
                ordem.append(Adjacente(eu, 0))

        ordem.reverse()

        caminho = list(ordem)

        aux = 0

        print('------------------------------------------------------------------------')
        print(caminho)
        for ca in caminho:
            aux += 1
            dist += ca.distancia
            if aux == 1:
                print('Embarque: {}'.format(ca.cidade.nome))
            else:
                item_rota = dict(
                    {
                        "ordem": aux - 1,
                        "cidade": ca.cidade.nome,
                        "distancia": ca.distancia
                    }
                )
                rota.append(item_rota)
                print('Destino {}:'.format(aux - 1), ca.cidade.nome, '| Distancia: {}'.format(ca.distancia))
            if aux == len(caminho):
                print('Distancia Total: {}'.format(dist), 'Quantidade de testes: {}'.format(busca.qtdtestes))
        print('------------------------------------------------------------------------')
    viagem = dict({
        "origem": cidades[id_origem].nome,
        "destino": cidades[id_destino].nome,
        "distancia_total": dist,
        "qtd_testes": busca.qtdtestes,
        "rota": rota
    })
    return jsonify(dict(viagem))


@app.route("/busca", methods=['GET'])
def busca():
    cidds = Mapa.lista_cidades()
    # id_origem = busca_origem(cidds)
    id_origem = 0
    id_destino = 0
    if id_origem >= 0:
        # id_destino = busca_destino(cidds)

        if id_destino >= 0:
            print('\n\n')
            print('Iniciando Procedimento de Busca em Profundidade.........................')
            busca_profundidade(id_origem, id_destino)
            print('Iniciando Procedimento de Busca em Largura.........................')
            busca_largura(id_origem, id_destino)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
