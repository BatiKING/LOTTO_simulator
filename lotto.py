import random


def lotto():
    """Function simulating LOTTO system - asking user for 6 numbers from 1-49 range
     and randomly picking 6 winning numbers that are later compared"""
    player_numbers = []
    winning_numbers = []
    while len(player_numbers) < 6:
        number = input(f"{len(player_numbers) + 1} number: ")
        try:
            number = int(number)
        except ValueError:
            print("Not a valid number!")
            continue
        if number not in range(1, 50):
            print("Provide a number in range 1-49")
            continue
        if number in player_numbers:
            print("Do not repeat numbers please")
            continue
        player_numbers.append(number)
    player_numbers.sort()
    print(f"Your numbers: \n" + ", ".join([str(x) for x in player_numbers]) + "\n")
    winning_numbers = [x for x in range(1, 50)]
    random.shuffle(winning_numbers)
    winning_numbers = winning_numbers[:6]
    print(f"Winning numbers: \n" + ", ".join([str(x) for x in winning_numbers]) + "\n")
    hit_counter = 0
    for player_number in player_numbers:
        if player_number in winning_numbers:
            hit_counter += 1
    # correct plural syntax
    s = 's' if hit_counter > 1 else ''
    print(f"You've hit {hit_counter} number{s}!")


lotto()
