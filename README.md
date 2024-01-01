<h1>Desafio 22 - Consulta de Capitais de Países em um Dicionário</h1>
<p>Este código tem como objetivo armazenar informações sobre as capitais de alguns países em um dicionário, permitir que o usuário informe um país e, em seguida, verificar se o país está presente no dicionário para exibir a capital correspondente.</p>

<ol>
<h2><li>Criação do Dicionário:</li></h2>
<ul>
<li>Inicia a variável informações com um dicionário contendo pares de países e suas respectivas capitais.</li>
</ul>

    informações = {
    'Brasil': 'Brasília',
    'Espanha': 'Madrid',
    'Portugal': 'Porto',
    'Colômbia': 'Bogotá',
    'Chile': 'Santiago'
    }

<h2><li>Entrada do Usuário</li></h2>
<ul>
    <li>Utiliza a função input para permitir que o usuário informe o nome do país desejado.</li>
    <li>Converte a entrada para o formato de título (capitalize()) para garantir consistência na comparação.</li>
</ul>

    pesquisa = input('Informe o país para ver a capital: ').capitalize()


<h2><li>Loop for para Pesquisa:</li></h2>
<ul>
    <li>Utiliza um loop for para iterar sobre cada par de chave e valor no dicionário.</li>
</ul>

    for key, value in informações.items():

<h2><li>Condição de Verificação:</li></h2>
<ul>
    <li>Dentro do loop, verifica se o país informado pelo usuário está presente no dicionário.</li>
    <li>Se o país estiver presente, imprime a capital correspondente e utiliza break para encerrar o loop.</li>
    <li>Caso contrário, imprime uma mensagem informando que não há informações sobre a capital do país.
    python
    </li>
</ul>

    if pesquisa in key:
        print(f'A capital de {key} é {value}')
        break
    else:
        print("Desculpe, não temos informações sobre a capital desse país.")
        break
</ol>

<h3>Mensagens Personalizadas:</h3>
<li>Capital Encontrada: Se o país informado estiver no dicionário, imprime a capital correspondente.
</li>
<li>Sem Informações: Se o país informado não estiver no dicionário, imprime uma mensagem indicando a ausência de informações.</li>

<h3>Interatividade:</h3>
<p>O código proporciona uma experiência interativa ao permitir que o usuário consulte a capital de um país específico no dicionário.</p>


<h3>Conclusão:</h3>
<p>
    Ao executar este código, o usuário receberá a capital correspondente ao país informado ou uma mensagem indicando a ausência de informações para o país consultado. Isso destaca o uso de dicionários e estruturas condicionais em Python.
</p>