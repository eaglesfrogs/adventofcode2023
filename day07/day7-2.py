files = open('day07/day7data.txt', 'r')
lines = files.readlines()

card_mask_map = {
    'J': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i',
    'T': 'j',
    'Q': 'k',
    'K': 'l',
    'A': 'm'
}


class Hand:

    def __init__(self, hand, bet) -> None:
        self.hand = hand
        self.bet = bet

        hand_rank = self.get_hand_rank()
        hand_mask = self.get_mask()

        self.mask = hand_rank + hand_mask

    def get_mask(self):
        mask = ''

        for c in self.hand:
            mask = mask + card_mask_map[c]

        return mask

    def get_hand_rank(self):
        hand_map = {}

        for c in self.hand:
            if c in hand_map:
                hand_map[c] = hand_map[c] + 1
            else:
                hand_map[c] = 1

        if 'J' in hand_map:
            j_count = hand_map['J']
            del hand_map['J']

            for h in hand_map:
                hand_map[h] = hand_map[h] + j_count

        count = list(hand_map.values())
        count.sort()

        if len(count) == 0 or (len(count) == 1 and count == [5]):
            # five of a kind
            return 'g'
        if len(count) == 2 and 4 in hand_map.values():
            # four of a kind
            return 'f'
        if len(count) == 2 and (count == [3, 3] or count == [2, 3]):
            # full house
            return 'e'
        if len(count) == 3 and 3 in hand_map.values():
            # three of a kind
            return 'd'
        if len(count) == 3 and count == [1, 2, 2]:
            # two pairs
            return 'c'
        if len(count) == 4 and (count == [2, 2, 2, 2] or count == [1, 1, 1, 2]):
            # one pair
            return 'b'

        # high card
        return 'a'


hands = []

for line in lines:
    segments = line.strip().split(' ')
    hand = Hand(segments[0], int(segments[1]))

    hands.append(hand)

sorted_hands = sorted(hands, key=lambda h: h.mask)

total = 0

for i in range(len(sorted_hands)):
    total = total + ((i+1) * sorted_hands[i].bet)

print(total)
