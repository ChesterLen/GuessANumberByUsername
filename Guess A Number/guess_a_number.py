import random
computer_number = random.randint(1, 100)
guess_count = 0
guess_limit = 10
while True:
    player_input = input("Guess a number (1-100): ")
    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue
    else:
        player_input = int(player_input)
        guess_count += 1
        if guess_count == guess_limit:
            print("You lose...")
            play_again = input("Do you want to play again? Type: 'y' for 'yes' or 'n' for 'no': ")
            if play_again == "y":
                guess_count = 0
                continue
            else:
                print("Bye!")
            break
    if player_input == computer_number:
        print("You guess it!")
        play_again = input("Do you want to play again? Type: 'y' for 'yes' or 'n' for 'no': ")
        if play_again == "y":
            guess_count = 0
            continue
        else:
            print("Bye!")
            break
    elif player_input > computer_number:
        print("Too high!")
        continue
    else:
        print("Too low!")
        continue
