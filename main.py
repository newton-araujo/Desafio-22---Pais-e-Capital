'''
Para este desafio, vamos criar um dicionário que tenha 5 paises e capitais.

O que o programa deverá fazer?
- Receber uma entrada buscando o pais.
- Realizar a busca e trazer a capital.
- Caso o pais não esteja cadastrada o sistema retorna uma msg de erro.


Saida esperada:
- "A capital de [país] é [capital]."
- "Desculpe, não temos informações sobre a capital desse país."

'''

#Informações cadastrada em nosso sistema.
informações = {
    'Brasil':'Brasilia',
    'Espanha':'Madrid',
    'Portugal':'Porto',
    'Colombia':'Bogota',
    'Chile':'Santiago'
}

#Entrada do usuário:
pesquisa = input('Informe o país para ver a capital: ').capitalize()


#Loop for interando cada elemento do dicionário, para achar a pesquisa.
for key, value in informações.items():
    #Condição para verificar se país esta presente na lista.
    if pesquisa in key:
        #Saida.
        print(f'A capital de {key} é {value}')
        break
    else:
        print("Desculpe, não tempos informações sobre a capital desse país.")
        break