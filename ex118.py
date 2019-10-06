# shuffling a deck of cards
import random

def creatingDeck():
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suits = ['S', 'H', 'D', 'C']
    list = []
    for s in suits:
        for v in values:
            l = s + v
            list.append(l)
    return list

def shuffle(cards):
    shuffled = []
    n = len(cards)-1
    while n >= 0:
        c = random.randint(0,n)
        shuffled.append(cards[c])
        cards.remove(cards[c])
        n -= 1
    return shuffled

def main():
    cards = creatingDeck()
    print("The shuffled deck of cards: ")
    print(" ".join(shuffle(cards)))

if __name__ == "__main__":
    main()
