import random

numeroAleatorio = random.randint(1, 50)

print("Jogo do Número Secreto")
print("Digite um número entre 1 e 50")

numeroTentativa = 5

for tentativas in range(numeroTentativa):
    numeroDigitado = int(input(f"Tentativas {tentativas + 1}: Digite um número: "))
    
    if numeroDigitado == numeroAleatorio:
        print("Parabéns! Você acertou o número!")
        break
    elif numeroDigitado < numeroAleatorio:
        print("O número secreto é maior. ")
    else:
        print("O número secreto é menor. ")
else:
    print(f"Jogo encerrado. O número secreto era {numeroAleatorio}")