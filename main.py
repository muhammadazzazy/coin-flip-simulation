import random
from sys import exit


def display(counts: dict[str: int]) -> None:
    print(f'\nNumber of heads: {counts['head']}')
    print(f'Number of tails: {counts['tail']}')
    print(f'Number of coin flips: {sum(counts.values())}')


def main() -> None:
    print('Welcome to The 🪙 Flip Simulator!')
    outcomes: list[str] = ['head', 'tail']
    counts: dict[str: int] = {outcomes[0]: 0, outcomes[1]: 0}
    exit_message: str = 'Exiting program...'
    while True:
        try:
            user_input: str = input('Flip a coin? (Y/n) ')
        except KeyboardInterrupt:
            display(counts)
            print(exit_message)
            exit()

        if user_input.lower() == 'y':
            outcome: str = random.choice(outcomes)
            print(f'{outcome.capitalize()}')
            if outcome == 'head':
                counts[outcomes[0]] += 1
            else:
                counts[outcomes[1]] += 1
        else:
            display(counts)
            exit()


if __name__ == '__main__':
    main()
