class CalculoCargas:

    def calculoEscolhaA(comprimento, carga):
        distanciaForca = comprimento/2
        quantidadeForca = carga * comprimento
        calculo = [distanciaForca, quantidadeForca]
        return calculo


    def calculoEscolhaB(comprimento, carga):
        distanciaForca = comprimento* 2/3
        quantidadeForca = carga * comprimento/2
        calculo = [distanciaForca, quantidadeForca]
        return calculo


    def calculoEscolhaC(comprimento, carga1, carga2):
        distanciaCarga1 = comprimento/2
        intensidadeCarga1 = carga1 * comprimento
        distanciaCarga2 = comprimento* 2/3
        intensidadeCarga2 = (carga2 - carga1) * comprimento/2
        calculo = [[intensidadeCarga1, distanciaCarga1],[intensidadeCarga2, distanciaCarga2]]
        return calculo