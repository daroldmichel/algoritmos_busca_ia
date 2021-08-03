from Cidade import Cidade, Adjacente


def lista_cidades():

    #Cria os objetos das Cidades
    aracaju = Cidade("Aracajú")
    belem = Cidade("Belém")
    belo_horizonte = Cidade("Belo Horizonte")
    boa_vista = Cidade("Boa Vista")
    brasilia = Cidade("Brasília")
    campo_grande = Cidade("Campo Grande")
    cuiaba = Cidade("Cuiabá")
    curitiba = Cidade("Curitiba")
    florianopolis = Cidade("Florianópolis")
    fortaleza = Cidade("Fortaleza")
    goiania = Cidade("Goiânia")
    joao_pessoa = Cidade("João Pessoa")
    macapa = Cidade("Macapá")
    maceio = Cidade("Maceió")
    manaus = Cidade("Manaus")
    natal = Cidade("Natal")
    palmas = Cidade("Palmas")
    porto_alegre = Cidade("Porto Alegre")
    porto_velho = Cidade("Porto Velho")
    recife = Cidade("Recife")
    rio_branco = Cidade("Rio Branco")
    rio_de_janeiro = Cidade("Rio de Janeiro")
    salvador = Cidade("Salvador")
    sao_luis = Cidade("São Luis")
    sao_paulo = Cidade("São Paulo")
    teresina = Cidade("Teresina")
    vitoria = Cidade("Vitória")

    #aplica o caminho
    aracaju.addCidadeAdjacente(Adjacente(maceio, 201))
    aracaju.addCidadeAdjacente(Adjacente(salvador, 277))

    belem.addCidadeAdjacente(Adjacente(macapa, 329))
    belem.addCidadeAdjacente(Adjacente(manaus, 1292))

    belo_horizonte.addCidadeAdjacente(Adjacente(rio_de_janeiro, 339))
    belo_horizonte.addCidadeAdjacente(Adjacente(sao_paulo, 489))
    belo_horizonte.addCidadeAdjacente(Adjacente(brasilia, 624))

    boa_vista.addCidadeAdjacente(Adjacente(manaus, 661))

    brasilia.addCidadeAdjacente(Adjacente(palmas, 620))
    brasilia.addCidadeAdjacente(Adjacente(goiania, 173))
    brasilia.addCidadeAdjacente(Adjacente(cuiaba, 1081))
    brasilia.addCidadeAdjacente(Adjacente(belo_horizonte, 624))
    brasilia.addCidadeAdjacente(Adjacente(sao_paulo, 873))
    brasilia.addCidadeAdjacente(Adjacente(manaus, 1932))
    brasilia.addCidadeAdjacente(Adjacente(fortaleza, 1687))

    campo_grande.addCidadeAdjacente(Adjacente(cuiaba, 559))
    campo_grande.addCidadeAdjacente(Adjacente(curitiba, 780))

    cuiaba.addCidadeAdjacente(Adjacente(campo_grande, 559))
    cuiaba.addCidadeAdjacente(Adjacente(porto_velho, 1137))
    cuiaba.addCidadeAdjacente(Adjacente(brasilia, 873))
    cuiaba.addCidadeAdjacente(Adjacente(sao_paulo, 1326))

    curitiba.addCidadeAdjacente(Adjacente(campo_grande, 559))
    curitiba.addCidadeAdjacente(Adjacente(sao_paulo, 338))
    curitiba.addCidadeAdjacente(Adjacente(florianopolis, 251))

    florianopolis.addCidadeAdjacente(Adjacente(curitiba, 251))
    florianopolis.addCidadeAdjacente(Adjacente(porto_alegre, 376))

    fortaleza.addCidadeAdjacente(Adjacente(sao_luis, 652))
    fortaleza.addCidadeAdjacente(Adjacente(teresina, 495))
    fortaleza.addCidadeAdjacente(Adjacente(brasilia, 1687))
    fortaleza.addCidadeAdjacente(Adjacente(salvador, 1028))
    fortaleza.addCidadeAdjacente(Adjacente(natal, 435))
    fortaleza.addCidadeAdjacente(Adjacente(recife, 629))

    goiania.addCidadeAdjacente(Adjacente(brasilia, 173))

    joao_pessoa.addCidadeAdjacente(Adjacente(natal, 151))
    joao_pessoa.addCidadeAdjacente(Adjacente(recife, 104))

    macapa.addCidadeAdjacente(Adjacente(belem, 329))

    maceio.addCidadeAdjacente(Adjacente(aracaju, 201))
    maceio.addCidadeAdjacente(Adjacente(recife, 202))

    manaus.addCidadeAdjacente(Adjacente(boa_vista, 661))
    manaus.addCidadeAdjacente(Adjacente(belem, 1292))
    manaus.addCidadeAdjacente(Adjacente(brasilia, 1932))
    manaus.addCidadeAdjacente(Adjacente(porto_velho, 761))
    manaus.addCidadeAdjacente(Adjacente(rio_branco, 1149))

    natal.addCidadeAdjacente(Adjacente(fortaleza, 435))
    natal.addCidadeAdjacente(Adjacente(joao_pessoa, 151))
    natal.addCidadeAdjacente(Adjacente(salvador, 875))

    palmas.addCidadeAdjacente(Adjacente(brasilia, 620))

    porto_alegre.addCidadeAdjacente(Adjacente(florianopolis, 376))

    porto_velho.addCidadeAdjacente(Adjacente(cuiaba, 1137))
    porto_velho.addCidadeAdjacente(Adjacente(manaus, 761))
    porto_velho.addCidadeAdjacente(Adjacente(rio_branco, 449))

    recife.addCidadeAdjacente(Adjacente(joao_pessoa, 104))
    recife.addCidadeAdjacente(Adjacente(maceio, 202))
    recife.addCidadeAdjacente(Adjacente(fortaleza, 629))

    rio_branco.addCidadeAdjacente(Adjacente(porto_velho, 449))
    rio_branco.addCidadeAdjacente(Adjacente(manaus, 1149))

    rio_de_janeiro.addCidadeAdjacente(Adjacente(vitoria, 412))
    rio_de_janeiro.addCidadeAdjacente(Adjacente(salvador, 1209))
    rio_de_janeiro.addCidadeAdjacente(Adjacente(belo_horizonte, 339))
    rio_de_janeiro.addCidadeAdjacente(Adjacente(sao_paulo, 357))

    salvador.addCidadeAdjacente(Adjacente(rio_de_janeiro, 1209))
    salvador.addCidadeAdjacente(Adjacente(fortaleza, 1028))
    salvador.addCidadeAdjacente(Adjacente(natal, 875))
    salvador.addCidadeAdjacente(Adjacente(aracaju, 277))

    sao_luis.addCidadeAdjacente(Adjacente(fortaleza, 652))

    sao_paulo.addCidadeAdjacente(Adjacente(curitiba, 338))
    sao_paulo.addCidadeAdjacente(Adjacente(cuiaba, 1326))
    sao_paulo.addCidadeAdjacente(Adjacente(brasilia, 873))
    sao_paulo.addCidadeAdjacente(Adjacente(belo_horizonte, 489))
    sao_paulo.addCidadeAdjacente(Adjacente(rio_de_janeiro, 357))

    teresina.addCidadeAdjacente(Adjacente(fortaleza, 495))

    vitoria.addCidadeAdjacente(Adjacente(rio_de_janeiro, 412))

    cidade = []
    cidade.append(aracaju)
    cidade.append(belem)
    cidade.append(belo_horizonte)
    cidade.append(boa_vista)
    cidade.append(brasilia)
    cidade.append(campo_grande)
    cidade.append(cuiaba)
    cidade.append(curitiba)
    cidade.append(florianopolis)
    cidade.append(fortaleza)
    cidade.append(goiania)
    cidade.append(joao_pessoa)
    cidade.append(macapa)
    cidade.append(maceio)
    cidade.append(manaus)
    cidade.append(natal)
    cidade.append(palmas)
    cidade.append(porto_alegre)
    cidade.append(porto_velho)
    cidade.append(recife)
    cidade.append(rio_branco)
    cidade.append(rio_de_janeiro)
    cidade.append(salvador)
    cidade.append(sao_luis)
    cidade.append(sao_paulo)
    cidade.append(teresina)
    cidade.append(vitoria)

    return cidade
