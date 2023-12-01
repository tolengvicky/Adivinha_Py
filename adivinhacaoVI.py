import random

total_de_tentativas = 5
rodada = 1

#loop
while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) # - isso é uma *interpolação de strings* ,substituiu  print("Tentativa", rodada, "de", total_de_tentativas) no III 
    chute_str = input("Digite un número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    numero_secreto = random.randrange(1,101)
    print=(numero_secreto)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if (chute < 1 or chute > 100): #limitação do numero a ser digitado
        print("Você deve digitar um número entre 1 e 100!")
        continue #não faz sentido continuarmos executando o código do loop se o valor não estiver no intervalo exigido. O que queremos não é sair do laço, e sim continuar para a próxima rodada, acabando com a iteração.

    #condicional if else elif
    if (acertou):
        print("Você acertou!")
        break # faz com que saiamos do laço
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo")
