

jogador = input('Id do jogador: ')

jogador = jogador.upper()

jogador_pontos = 12000

pontos_jogador = int(input('Informe a quantidade de pontos do jogador com base no seu id: '))

if jogador_pontos != pontos_jogador:
    print('Contagem incorreta!')
else:
    print('Contagem correta, processando pontos...')

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
