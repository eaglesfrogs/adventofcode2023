import re


files = open('day04/day4data.txt', 'r')
lines = files.readlines()


class Card:

    def __init__(self, winning_nums, player_nums) -> None:
        self.winning_nums = winning_nums
        self.player_nums = player_nums
        self.winning_nums.sort()
        self.player_nums.sort()
        self.num_cards = 1

    def get_score(self):
        count = 0

        for num in self.player_nums:
            if num in self.winning_nums:
                count = count + 1

        if count == 0:
            return {'count': count, 'score': 0}

        return {'count': count, 'score': 2 ** (count - 1)}

    def inc_cards(self, count):
        self.num_cards = self.num_cards + count


cards = []

for line in lines:
    winning_nums = re.findall(r'[0-9]+', line[10:40])
    player_nums = re.findall(r'[0-9]+', line[42:117])

    cards.append(Card(winning_nums, player_nums))

total_score = 0
total_cards = 0

for i in range(len(cards)):
    card = cards[i]

    score = card.get_score()

    total_score = total_score + score['score']
    total_cards = total_cards + card.num_cards

    for j in range(score['count']):
        cards[i + j + 1].inc_cards(card.num_cards)

print(
    f"Total score (part 1): {total_score}.  Total cards (part 2): {total_cards}")
