NomeDoHeroi = ''         #Declaração de Variáveis
xp = ''
nivel = ''

while True:	            #Laço de Repetição

    NomeDoHeroi = input('Insira o nome do seu herói: ')
    xp = input('Insira o XP do seu herói: ')

    if NomeDoHeroi == '' or xp == '' or xp == 0:			#Estrutura de Decisão
        print('\n(FAVOR INSERIR CORRETAMENTE AS INFORMAÇÕES)\n')	
        continue
    elif NomeDoHeroi != '' or xp != 0:
        break
xp = int(xp)		       #Convertendo o Tipo da Variável XP para Entrada com Tipo Inteiro

if xp <= 1000:		#Uso de Operadores
        nivel = 'Ferro'
elif xp >= 1001 and xp <= 2000:
        nivel = 'Bronze'
elif xp >= 2001 and xp <= 5000:
        nivel = 'Prata'
elif xp >= 5001 and xp <= 7000:
        nivel = 'Ouro'
elif xp >= 7001 and xp <= 8000:
        nivel = "Platina"
elif xp >= 8001 and xp <= 9000:
        nivel = "Ascendente"
elif xp >= 9001 and xp <= 10000:
        nivel = 'Imortal'
elif xp >= 10001:
        nivel = 'Radiante'

if NomeDoHeroi != '' and xp != '':
        print('O herói de nome {} está no nível de {}'.format(NomeDoHeroi, nivel))
