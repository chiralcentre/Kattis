G,S,C = map(int,input().split())
buying_power = G*3 + S*2 + C*1
victory_cards = {8:'Province',5:'Duchy',2:'Estate'}
treasure_cards = {6:'Gold',3:'Silver',0:'Copper'}
lst = list(filter(lambda x: x <= buying_power,victory_cards.keys()))
print(f'{victory_cards[max(lst)]} or {treasure_cards[max(list(filter(lambda x: x <= buying_power,treasure_cards.keys())))]}') if len(lst) > 0 else print(treasure_cards[max(list(filter(lambda x: x <= buying_power,treasure_cards.keys())))])
