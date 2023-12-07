files = open('day07/day7data.txt', 'r')
lines = files.readlines()

card_mask_map = {
    '2': 'a',
    '3': 'b',
    '4': 'c',
    '5': 'd',
    '6': 'e',
    '7': 'f',
    '8': 'g',
    '9': 'h',
    'T': 'i',
    'J': 'j',
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

        count = list(hand_map.values())
        count.sort()

        if len(count) == 1 and count == [5]:
            # five of a kind
            return 'g'
        if len(count) == 2 and count == [1, 4]:
            # four of a kind
            return 'f'
        if len(count) == 2 and count == [2, 3]:
            # full house
            return 'e'
        if len(count) == 3 and count == [1, 1, 3]:
            # three of a kind
            return 'd'
        if len(count) == 3 and count == [1, 2, 2]:
            # two pairs
            return 'c'
        if len(count) == 4 and count == [1, 1, 1, 2]:
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
