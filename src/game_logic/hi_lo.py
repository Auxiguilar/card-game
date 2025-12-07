from src.cards.card_class import Card
from src.cards.deck_class import Deck


def get_player_guess() -> str:
    '''Takes an input until a valid one is given. 10 tries before the loop breaks with an error.'''

    print('Make a guess:')
    i = 0

    while i < 10:
        guess: str = input('> ').strip().lower()
    
        if guess == 'hi' or guess == 'high' or guess == 'higher':
            return 'gt'
        if guess == 'eq' or guess == 'equal' or guess == 'equals' or guess == 'tie':
            return 'eq'
        if guess == 'lo' or guess == 'low' or guess == 'lower':
            return 'lt'
        
        i += 1

    # only because it seems absurd to let it run too long...
    raise RuntimeError(f'Too many tries: {i}.')

def player_continue() -> bool:
    confirm: str = input('Continue? (Y/n)\n> ').strip().lower()
    result: bool = True

    if confirm == 'n' or confirm == 'no':
        result = False
    
    return result
        
def compare_cards(drawn_card: Card, snap_card: Card, guess: str) -> bool:
    result: bool = False

    if guess == 'gt':
        result = drawn_card > snap_card
    elif guess == 'lt':
        result = drawn_card < snap_card
    elif guess == 'eq':
        result = drawn_card.value == snap_card.value
    else:
        raise ValueError(f'Invalid guess: "{guess}". Must be "gt", "lt", or "eq".')

    return result

def hi_lo_game():
    deck: Deck = Deck()

    deck.shuffle()
    snap_card: Card = deck.draw()

    wins, losses = 0, 0

    while True:
        if not deck:
            deck: Deck = Deck()
            deck.shuffle()

        print(f'\nW: {wins}, L: {losses}')
        drawn_card: Card = deck.draw()

        print(f'\nSnap card: {str(snap_card)}\nDrawn card: ???')
        player_guess: str = get_player_guess()
        
        print(f'\nSnap card: {str(snap_card)}\nDrawn card: {str(drawn_card)}')
        result: bool = compare_cards(drawn_card, snap_card, player_guess)

        if result:
            wins += 1
            print('Correct guess! >>> W <<<\n')
        else:
            losses += 1
            print('Wrong guess! >>> L <<<\n')

        if not player_continue():
            break

        for i in range(3):
            if not deck:
                deck: Deck = Deck()
                deck.shuffle()

            deck.draw()

        snap_card = drawn_card
