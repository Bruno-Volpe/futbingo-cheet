players = {}
remits = {}

def find_correspondence(player, remits):
    possible_numbers = [player.get('f'), player.get('g'), player.get('i'), player.get('c')]
    possible_numbers.extend(player.get('m', {}).values())
    possible_numbers.extend(player.get('s', {}).values())
    possible_numbers.extend(player.get('t', {}).values())
    
    for key, value in remits.items():
        for num in possible_numbers:
            if num and num == value.get('id'):
                return value
    return None
# Relacionando os jogadores do objeto 2 com o objeto 1
for key, player in players.items():
    correspondence = find_correspondence(player, remits)
    print(f"Jogador {player['f']} {player['g']} está relacionado com {correspondence}")
