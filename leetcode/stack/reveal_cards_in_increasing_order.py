from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        temp = [i for i in range(len(deck))] 
        temp2 = []
        answer = [0 for i in range(len(deck))]

        while(temp) :
            temp2.append(temp.pop(0))
            
            if temp:
                temp.append(temp.pop(0))

        deck = sorted(deck)

        for i in temp2:
            answer[i] = deck.pop(0)

        return answer





# solution 2

import collections


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        d = collections.deque()
        deck.sort(reverse=True)
        for i in deck:
            if d:
                d.appendleft(d.pop())
            d.appendleft(i)
        return list(d)

"""
[2,13,3,11,5,17,7]
[3,11,5,17,7,13]    [2]
[5,17,7,13,11]      [2,3]
[7,13,11,17]        [2,3,5]
[11,17,13]          [2,3,5,7]
[13,17]             [2,3,5,7,11]
[17]                [2,3,5,7,11,13]
[]                  [2,3,5,7,11,13,17]
"""