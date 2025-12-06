import sys


def main():
    print("Hello from card-game!")

    from src.game_logic.hi_lo import hi_lo_game

    try:
        hi_lo_game()
    except Exception as e:
        print(f'Something went wrong: {e}')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nExiting game...')
        sys.exit(0)
