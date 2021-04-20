def main():
    comprimento = float(input("Qual o comprimento da barra? "))

    print("Qual a representação das cargas sobre o corpo?")
    print("A) Uniformemente distribuída")
    print("B) Uniformemente variável, onde q1 = 0 e q2 > q1")
    print("C) Uniformemente variável, onde q1 > 0 e q2 > q1")
    userChoice = input()

    while (userChoice != "A") and (userChoice != "a") and (userChoice != "B") and (userChoice != "b") \
            and (userChoice != "C") and (userChoice != "c"):
        print(userChoice != "a")
        print(userChoice != "A")
        userChoice = input("Por favor digite uma alternativa válida: ")

    escolhaUsuario(comprimento, userChoice)




def escolhaUsuario (comprimento, userChoice):
    if userChoice == "A" or userChoice == "a":
        carga = float(input("Por favor, digite a carga: "))
        calculo = calculoEscolhaA(comprimento, carga)
        impressaoValores(1, calculo)


    elif userChoice == "B" or userChoice == "b":
        carga = float(input("Por favor, digite a carga: "))
        calculo = calculoEscolhaB(comprimento, carga)
        impressaoValores(1, calculo)


    elif userChoice == "C" or userChoice == "c":
        carga1 = float(input("Por favor, digite a carga da primeira força: "))
        carga2 = float(input("Por favor, digite a carga da segunda força: "))
        calculo = calculoEscolhaC(comprimento, carga1, carga2)
        impressaoValores(2, calculo)


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
    distanciaForca1 = comprimento/2
    quantidadeForca1 = carga1 * comprimento
    distanciaForca2 = comprimento* 2/3
    quantidadeForca2 = (carga2 - carga1) * comprimento/2
    calculo = [[quantidadeForca1, distanciaForca1],[quantidadeForca2, distanciaForca2]]
    return calculo


def impressaoValores(tipoResposta, calculo):
    if tipoResposta == 1:
        print("Intensidade da força resultante: ", calculo[1])
        print("Distância onde a força será aplicada: ", calculo[0])

    elif tipoResposta == 2:
        print("\nIntensidade das forças resultantes:"
              "\n    Força 1: {0}"
              "\n    Força 2: {1}".format(calculo[0][0], calculo[1][0]))
        print("Distância onde as forças serão aplicadas:"
              "\n    Força 1: {0}"
              "\n    Força 2: {1}".format(calculo[0][1], calculo[1][1]))


#main()