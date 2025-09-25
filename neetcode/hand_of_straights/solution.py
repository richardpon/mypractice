from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # in each iteration attempt to create a hand
        # get minumum card
        # get groupSize-1 more cards
        card_counts = Counter(hand)
        while card_counts:
            start = min(card_counts.keys())

            for i in range(groupSize):
                cur_card = start + i

                if (cur_card) not in card_counts:
                    return False
                    
                card_counts[cur_card] -= 1
                if card_counts[cur_card] == 0:
                    del card_counts[cur_card]

        return True
        

