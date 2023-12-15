# Read data from the text file
with open('input.txt', 'r') as file:
    lines = file.readlines()

hand_dict = {}

for counter, line in enumerate(lines) :
    cards, bid = line.split()
    hand_dict[counter] = {'cards': cards, 'rank': -1, 'bid': int(bid), 'handtype':-1}



# 1 = 5 of a kind, 2 = four of a kind, 3 = Full house, 4 = three of a kind,  5 = two pairs, 6 = pair, 7 = highcard

def get_hand_type(cards) :
    card_counts = {}
    for c in cards :
        if c in card_counts :
            card_counts[c] += 1
        else:
            card_counts[c] = 1

    sorted_cards = sorted(card_counts.values(), reverse=True)
    if sorted_cards[0] == 5:
        return 6
    elif sorted_cards[0] == 4:
        return 5
    elif sorted_cards[0] == 3 and sorted_cards[1] == 2:
        return 4
    elif sorted_cards[0] == 3 :
        return 3
    elif sorted_cards[0] == 2 and sorted_cards[1] == 2:
        return 2
    elif sorted_cards[0] == 2 and sorted_cards[1] == 1:
        return 1
    return 0

card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}

def card_value(card) :
    return -int(card_values.get(card, card) ) # Use negation for descending order


for hand_id, hand_info in hand_dict.items():
    hand_info['handtype'] = get_hand_type(hand_info['cards'])

sorted_hands = []
for i in range(7):
    matching_hands = [hand for hand in hand_dict.values() if hand['handtype'] == i]
    if len(matching_hands) == 1 :
        matching_hands[0]['rank'] = len(sorted_hands) + 1
        sorted_hands.append(matching_hands[0])
    elif len(matching_hands) > 1 :
        ## Sort the hands by highets card
        sorted_array = sorted(matching_hands, key=lambda x: [card_value(card) for card in x['cards']], reverse=True)

        for item in sorted_array:
            item['rank'] = len(sorted_hands) + 1
            sorted_hands.append(item)

hand_value = [item['rank'] * item['bid'] for item in sorted_hands]


print(sum(hand_value))
# Sort the dictionary items based on 'handtype', 'rank', and the highest values in 'cards[0]'
