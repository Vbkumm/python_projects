from exe111.utilidadescash import dados, moeda

n = dados.leiaDinheiro("Diga o preço: R$ ")
moeda.resumo(n, 80, 35)