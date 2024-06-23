import random

def naive_algorithm():
    cards = [1, 2, 3, 4]
    for i in range(4):
        n = random.randrange(0, 4)
        cards[i], cards[n] = cards[n], cards[i]
    return cards

def fisher_yates_shuffle():
    cards = [1, 2, 3, 4]
    for i in range(3, 0, -1):
        n = random.randrange(0, i+1)
        cards[i], cards[n] = cards[n], cards[i]
    return cards

freq_naive = {}
freq_fisher_yates = {}
for i in range(1000000):
    #print("test")
    cards_naive = tuple(naive_algorithm())
    cards_fisher_yates = tuple(fisher_yates_shuffle())
    freq_naive[cards_naive] = freq_naive.get(cards_naive, 0) + 1
    freq_fisher_yates[cards_fisher_yates] = freq_fisher_yates.get(cards_fisher_yates, 0) + 1

kind =[(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4),
(2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4),
(3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2),
(4, 3, 2, 1)]

print("Naive algorithm:")
for index in kind:
    print(f"{index} : {freq_naive.get(index, 0)}")
print("\n")
print("Fisher–Yates shuffle:")
for index in kind:
    print(f"{index} : {freq_fisher_yates.get(index, 0)}")