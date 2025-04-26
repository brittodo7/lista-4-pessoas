# lista-4-pessoas uma lista de coleta nome idade e sexo de 4 pessoas e volta com a media de idade dessas pessoas, qual o homem mais velho e ha quantas mulheres com menos de 20 anos
import statistics
old = []
maiorhomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('------pessoa de numero',p,'-------')
    nome = input("nome: ")
    sexo = input("sexo: ")
    idade = int(input("idade: "))
    print()
    old.append(idade)
    
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
        
    if p== 1 and sexo == 'h':
        maiorhomem = idade
        nomevelho = nome
    else:
        continue
    if sexo == 'h' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome

media = statistics.mean(old)

print ('A media é: ', media)
print ('O homem mais velho é:',nomevelho, maiorhomem)
print('existem ', totmulher20,' mulhers com menos de 20 anos')
