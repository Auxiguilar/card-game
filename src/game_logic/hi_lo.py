from src.cards.card_class import Card
from src.cards.deck_class import Deck
from src.player.player_class import Player


def get_player_guess() -> str:
    '''Takes an input until a valid one is given. 10 tries before the loop breaks with an error. Returns "gt", "lt", or "eq".'''

    print('Make a guess:')
    i = 0

    while i < 10:
        guess: str = input('> ').strip().lower()
    
        if guess == 'hi' or guess == 'high' or guess == 'higher' or guess == '>':
            return 'gt'
        if guess == 'eq' or guess == 'equal' or guess == 'equals' or guess == 'tie' or guess == '=':
            return 'eq'
        if guess == 'lo' or guess == 'low' or guess == 'lower' or guess == '<':
            return 'lt'
        
        i += 1

    # Only because it seems absurd to let it run for too long...
    raise RuntimeError(f'Too many tries: {i}.')

def compare_cards(drawn_card: Card, snap_card: Card) -> str:
    '''Compares `drawn_card` with `snap card`, returning the correct answer as "gt", "lt", or "eq".'''

    if drawn_card > snap_card:
        return 'gt'
    if drawn_card < snap_card:
        return 'lt'
    return 'eq'


def player_continue() -> bool:
    '''Returns choice of the player as if to answer "continue?" with `True` or `False`.'''

    confirm: str = input('Continue? (Y/n)\n> ').strip().lower()
    if confirm == 'n' or confirm == 'no':
        return False
    return True

def hi_lo_game() -> None:
    print(
        '''
Guess whether the drawn card is higher,
or lower than, or equal to the snap card.
'''
    )

    deck: Deck = Deck()

    deck.shuffle()
    snap_card: Card = deck.draw_card()

    player: Player = Player(input('Your name?\n> ').strip())

    # Basically, draw a card from the deck, let the player guess how it
    # stacks up to the "snap card", then get the "truth", then compare
    # the two and decide the result for the player.

    # Mills 3 cards from the top of the deck, and throws them away
    # alongside the old snap card, making the previously drawn card
    # the new snap card.
    
    # Anyway, picking tie right now just means you lose about 95% of the
    # time, but with betting it might give much better returns when that
    # is implemented in the future.

    while True:
        if not deck:
            deck: Deck = Deck()
            deck.shuffle()

        print(f'\n{player.name}\'s score: {player.score}')
        drawn_card: Card = deck.draw_card()

        print(f'\nSnap card: {str(snap_card)}\nDrawn card: ???')
        player_guess: str = get_player_guess()
        
        print(f'\nSnap card: {str(snap_card)}\nDrawn card: {str(drawn_card)}')
        result: str = compare_cards(drawn_card, snap_card)

        if result == player_guess:
            player.score += 1
            print('Correct guess!\nScore +1\n')
        else:
            player.score -= 1
            print('Wrong guess!\nScore -1\n')

        if not player_continue():
            print(f'\n{player.name}\'s final score: {player.score}')
            break

        for i in range(3):
            if not deck:
                deck: Deck = Deck()
                deck.shuffle()

            deck.draw_card()

        snap_card = drawn_card
