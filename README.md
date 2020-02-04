# monopoly_simulator


## Descrição
O simulador de Banco Imobiliário foi criado conforme as seguintes especificações:
- O tabuleiro contém 20 casas, cada uma com um valor de compra (valor aleatório entre 200 e 550) e aluguel (25% do valor de compra), gerados quando o script é executado;
- Por questões de simplicidade, não é possível construir casas e hoteis nos espaços
- Quatro jogadores participam da partida e cada um deles tem uma personalidade específica:
*Impulsivo:* compra qualquer propriedade sobre a qual ele parar;
*Exigente:* compra qualquer propriedade sobre a qual ele parar, desde que o valor do aluguel dela seja maior do que 50;
*Cauteloso:* compra qualquer propriedade sobre a qual ele parar, desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra;
*Aleatório:* compra a propriedade que ele parar em cima com probabilidade de 50%
- Os jogadores jogam turnos alternados rolando um dado de seis faces e andando a quantidade respectiva de espaços;
- Jogadores que cairem em espaços já controlados por outro jogador pagam a este o valor do aluguel correspondente;
- Todos os jogadores começam com 300 de dinheiro e ganham 100 caso completem uma volta no tabuleiro
- Jogadores com saldo negativo são eliminados do jogo
- A partida dura até sobrar um jogador só ou quando se passarem 1000 turnos, quando ela é encerrada e todos os jogadores ativos são considerados vitoriosos

## Pré requisitos:
Para rodar o script, é necessário apenas utilizar a versão 3 ou superior do Python. Nenhum outro módulo é necessário.
O comando é `python3 monopoly.py`

## Retorno do script:

`Maximum number of rounds before timeout: 1000` -> Número total de rodadas antes do timeout, pré configurado para 1000
`Running 300 simulations...` -> Número de simulações executadas, pré configurado para 300

`Results:`
`Avg. Rounds: 594.05` -> Média da duração da partida em turnos
`Total of matches ending with timeout: 144` -> Total de simulações encerradas com timeout, após o número limite de turnos
`Percentage of victory:` -> Porcentagem de vitórias de cada personalidade de jogador
             `impulsive: 33.33%`
             `demanding: 33.0%`
             `cautious: 61.67%`
             `random: 32.0%`

`player3 (cautious) won most times, with 185 victories` -> Jogador (e personalidade) com o maior número de vitórias em todas as simulações

