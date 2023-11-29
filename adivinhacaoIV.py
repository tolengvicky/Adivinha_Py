total_de_tentativas = 3
rodada = 1

#loop
while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) # - isso é uma *interpolação de strings* ,substituiu  print("Tentativa", rodada, "de", total_de_tentativas) no III 
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    numero_secreto = 42

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    #condicional if else elif

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo")