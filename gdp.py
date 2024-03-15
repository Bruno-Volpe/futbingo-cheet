players = {}
remits = {}

def find_correspondence(player, remits):
    possible_numbers = [player.get('f'), player.get('g'), player.get('i'), player.get('c')]
    possible_numbers.extend(player.get('m', {}).values())
    possible_numbers.extend(player.get('s', {}).values())
    possible_numbers.extend(player.get('t', {}).values())
    
    correspondences = []
    for key, value in remits.items():
        for num in possible_numbers:
            if num and num == value.get('id'):
                correspondences.append(value)
    return correspondences

# Relacionando os jogadores do objeto 2 com o objeto 1
for key, player in players.items():
    correspondences = find_correspondence(player, remits)
    if correspondences:
        print(f"Jogador {player.get('f')} {player.get('g')} está relacionado com:")
        for correspondence in correspondences:
            print(correspondence)
        print("\n")
    else:
        print(f"Nenhuma correspondência encontrada para jogador {player.get('f')} {player.get('g')}")
        print("\n")
