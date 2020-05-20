from Cards import Cards
import random

Deck = []
winStack = []
shuffles = 0
wins = 0
rounds = 0


def create_deck():
    for j in range(0, 4):  # color
        for i in range(7, 15):  # value
            Deck.append(Cards(j, i))
    random.shuffle(Deck)
    for color in range(4):
        winStack.append([Cards(color, 6)])


def create_stacks():
    length = int(len(Deck) / 3)
    if len(Deck) % 3 != 0:
        length += 1

    stacks = [[] for _ in range(length)]

    for stack in stacks:
        if len(Deck) >= 3:
            for _ in range(3):
                stack.append(Deck[0])
                Deck.pop(0)
        else:
            for _ in range(len(Deck)):
                stack.append(Deck[0])
                Deck.pop(0)
    return stacks


def print_stacks(stacks):
    for stack in stacks:
        print('-----------------')
        for card in stack:
            if card.value == 6:
                continue
            print(card.value, card.color)


def shuffle_cards(stacks):
    for stack in stacks:
        for card in stack:
            Deck.append(card)
    random.shuffle(Deck)
    update()


def lay_down_card(stacks):
    laid_down = False
    card_found = True
    while card_found:
        card_found = False
        for stack in stacks:
            try:
                if (stack[0].value - 1) == winStack[stack[0].color][-1].value:
                    card_found = True
                    laid_down = True
                    winStack[stack[0].color].append(stack[0])
                    stack.pop(0)
            except:
                continue
    return laid_down


def stock_cards(stacks):
    found = True
    while found:
        found = False
        for color in range(0, 4):
            for value in range(13, 6, -1):
                found_one, stack_one = check_stacks(stacks, color, value)
                if found_one:
                    found_two, stack_two = check_stacks(stacks, color, value + 1)
                    if found_two:
                        found = True
                        card = stacks[stack_one][0]
                        stacks[stack_one].pop(0)
                        stacks[stack_two].insert(0, card)


def check_stacks(stacks, color, value):
    for stack in range(len(stacks)):
        try:
            if stacks[stack][0].color == color and stacks[stack][0].value == value:
                return True, stack
        except:
            continue
    return False, None


def check_for_win(stacks):
    finished = 0
    for stack in stacks:
        try:
            if stack[-1].value == 14:
                finished += 1
        except:
            continue
    if finished == 4:
        global wins
        wins += 1
        auto_start()
        print("\n\n!!!!!! YOU WON !!!!!!")
        print_stacks(winStack)


def update():
    global shuffles
    shuffles += 1
    stacks = create_stacks()
    lay_down_card(stacks)
    stock_cards(stacks)

    while True:
        laid_down = lay_down_card(stacks)
        if laid_down:
            stock_cards(stacks)
        else:
            break

    check_for_win(winStack)
    if shuffles == 3:
        auto_start()
    shuffle_cards(stacks)


def auto_start():
    global rounds
    global shuffles
    global wins
    if rounds == 100:
        print("WINS: {}\nOUT OF: {}".format(wins, rounds))
        exit()
    rounds += 1
    Deck.clear()
    winStack.clear()
    shuffles = 0
    main()


def main():
    create_deck()
    update()


if __name__ == '__main__':
    main()
