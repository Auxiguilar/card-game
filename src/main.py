import sys


def main():
    print("Hello from card-game!")

    from src.game_logic.hi_lo import hi_lo_game

    try:
        hi_lo_game()
        print('\n\nExiting game...')
        sys.exit(0)

    except Exception as e:
        print(f'Something went wrong: {e}')
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
        
    except KeyboardInterrupt:
        print('\n\nExiting game...')
        sys.exit(0)
