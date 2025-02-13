import random


def main() -> None:
    outcomes: list[str] = ['head', 'tail']
    counts: dict[str: int] = {outcomes[0]: 0, outcomes[1]: 0}
    print('Welcome to The 🪙 Flip Simulator!')
    while True:
        user_input: str = input('Flip a coin? (Y/n) ')
        if user_input.lower() == 'y':
            outcome: str = random.choice(outcomes)
            print(f'{outcome.capitalize()}')
            if outcome == 'head':
                counts[outcomes[0]] += 1
            else:
                counts[outcomes[1]] += 1
        else:
            print(f'Number of heads: {counts[outcomes[0]]}')
            print(f'Number of tails: {counts[outcomes[1]]}')
            print(
                f'Number of coin flips: {counts[outcomes[0]]+counts[outcomes[1]]}')
            print('Thanks for trying my program!')
            exit()


if __name__ == '__main__':
    main()
