"""
Usado como referência o sistema de pontuação do jogo Apex legends.
Claramente isso não é nem perto de como o sistema de pontuação do jogo funciona,
minha intencão foi somente pegar como base para criar uma pequena lógica de programação

"""

jogador = input('Id do jogador: ')

pontos_jogador = int(input('Informe a quantidade de pontos do jogador com base no seu id: '))

system_rank_iniciante = 1000
system_rank_bronze = 3000
system_rank_prata = 5000
system_rank_ouro = 7000
system_rank_platina = 11400
system_rank_diamante = 15000
system_rank_mestre = 30000

pontos = pontos_jogador

if pontos <= system_rank_iniciante:
    print(f'Seu rank é iniciante')
elif pontos <= system_rank_bronze:
    print(f'Seu rank é bronze')
elif pontos <= system_rank_prata:
    print(f'Seu rank é prata')
elif pontos <= system_rank_ouro:
    print(f'Seu rank é ouro')
elif pontos <= system_rank_platina:
    print(f'Seu rank é platina')
elif pontos <= system_rank_diamante:
    print(f'Seu rank é diamante')
elif pontos <= system_rank_mestre:
    print(f'Seu rank é mestre')
else: 
    print('Seu rank é predador')
