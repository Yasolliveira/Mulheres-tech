'''print('Qual a sua idade?')
idade = int(input())

if idade >= 18:
    print('ACESSO LIBERADO! BOA FESTA!')
else:
    print('ACESSO NEGADO! VOCÊ É MENOR DE IDADE')'''

    # CÓDIGO PARA LIBERAR ACESSO SÓ PARA MAIORES DE 19 ANOS

'''print('Qual a sua idade?')
idade = int(input())

if idade < 18:
        print('ACESSO NEGADO! VOC~E É MENOR DE IDADE')
elif idade == 18:
        print("VOCÊ ESTÁ QUASE LÁ! MAIS UM ANO E VOCÊ TERÁ ACESSO")
else:
    print('ACESSO LIBERADO! BOA FESTA!')'''



'''print('Digite a nota do primeiro bimestre')
B1 = float(input())
print('Digite a nota do segundo bimestre')
B2 = float(input())
print('Digite a nota do terceiro bimestre')
B3 = float(input())
print('Digite a nota do quarto bimestre')
B4 = float(input())
media = (B1 + B2 + B3 + B4) / 4
print ('A média do aluno é ' , media)

print('Média final')
media = int(input())

if media >= 7:
    print('APROVADO')
elif media  >=5:
    print('RECUPERAÇÃO')
else: 
    print("REPROVADO")'''



'''print('Qual seu gênero? ( F OU M')
genero = input().upper()
print('Qual município você mora?')
municipio = input().lower()

if genero.upper() == 'F' and municipio.lower() == 'rio de janeiro':
    print('VOCÊ PODE PARTICIPAR DO MULHERES TECH')
else:
    print('VOCÊ NÃO PODE PARTICIPAR DO MULHERES TECH')'''


print('BEM VINDO AO CINEMA')
print(' ')
print('Qual sua idade?')
idade = int(input())

if idade >= 18:
    print('ACESSO LIBERADO!\nBOM FILME!')
elif idade >= 16:
    print('O FILME SELECIONADO É PARA MAIORES DE 18 ANOS\nPARA ACESSAR PRECISA ESTAR ACOMPONHADO DE UM RESPONSÁVEL. \nVOCÊ ESTÁ COM SEU RESPONSÁVEL?')
    responsavel = input().upper()
    if responsavel == 'SIM':
        print('ACESSO LIBERADO!\nBOM FILME')
    else:
        print('VOCÊ SÓ PODE VER O FILME ACOMPANHADO DE UM RESPONSÁVEL')

else:
    print('ACESSO NEGADO\n VOCÊ É MENOR DE IDADE!')
