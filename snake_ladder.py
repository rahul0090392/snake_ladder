import time
import random
import sys
from constants import (
    SLEEP_BETWEEN_ACTIONS,
    MAX_VAL,
    VALID_DICE,
    CROOKED_DICE,
    DICE_CHOICE,
    SNAKES,
    LADDERS,
    MAX_TURNS,
    player_turn_text,
    snake_bite,
    ladder_jump,
)


class Player:
    def __init__(self):
        self.current_position = 0
        self.old_position = 0
        self.turn = 0

    def get_set_player_name(self):
        self.name = None
        while not self.name:
            self.name = input("Please enter a valid name for first player: ").strip()

            print(f"All the best {self.name}")

    def update_position(self, current_position):
        self.current_position = current_position

    def increment_turn(self):
        self.turn += 1


class Dice:
    def __init__(self, dices):
        self.dices = dices
        self.selected_dice = None

    def set_selected_dice(self):

        while self.selected_dice not in self.dices.keys():
            print("We have two types of dice availabe \n1. Common \n2. Crooked \n")
            self.selected_dice = input(" Please Enter your selected dice: ").strip()

        self.selected_dice = self.dices[self.selected_dice]

    def get_rolled_dice_value(self):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        self.current_dice_value = random.choice(self.selected_dice)
        print("Its a " + str(self.current_dice_value))
        return self.current_dice_value


class SnakeGame:
    def __init__(self, snakes, ladders, max_value, max_turns):
        self.snakes = snakes
        self.ladders = ladders
        self.max_value = max_value
        self.max_turns = max_turns

    def print_welcome_message(self):
        msg = """
        Welcome to Snake and Ladder Game.
        Version: 1.0.0
        Developed by: Rahul Jain
        
        Rules:
        1. Initially you will be starting at position 0.
        2. Player can have 10 turns to win the game.
        3. There are two kinds of dice available to play with i.e, common and crooked.
        4. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
        5. If you lands on the head of a snake, you must slide down to the bottom of the snake.
        6. Hit enter to roll the dice.
        
        """
        print(msg)

    def print_snake_bite_message(self, player):
        print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
        print(
            "\n"
            + player.name
            + " got a snake bite. Down from "
            + str(player.old_position)
            + " to "
            + str(player.current_position)
        )

    def print_ladder_message(self, player):
        print("\n" + random.choice(ladder_jump).upper() + " ########")
        print(
            "\n"
            + player.name
            + " climbed the ladder from "
            + str(player.old_value)
            + " to "
            + str(player.current_value)
        )

    def is_snake_bite(self, player):
        if player.current_position in self.snakes:
            player.current_position = self.snakes[player.current_position]
            return True
        return False

    def is_ladder(self, player):
        if player.current_position in self.ladders:
            player.current_position = self.ladders[player.current_position]
            return True
        return False

    def print_winner_message(self, player):
        print("\n\n\nThats it.\n\n" + player.name + " won the game.")
        print("Congratulations " + player.name)
        print("\nThank you for playing the game.")

    def check_if_player_win(self, player):
        if self.max_value == player.current_position:
            return True

    def snake_ladder(self, player, dice_value):
        print(player.name + " moving....")
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        player.increment_turn()
        player.old_position = player.current_position
        player.current_position = player.current_position + dice_value

        if player.current_position > self.max_value:
            print(
                "You need "
                + str(self.max_value - player.old_position)
                + " to win this game. Keep trying."
            )
            return player.old_position

        print(
            "\n"
            + player.name
            + " moved from "
            + str(player.old_position)
            + " to "
            + str(player.current_position)
        )
        if self.is_snake_bite(player):
            self.print_snake_bite_message(player)

        if self.is_ladder(player):
            self.print_ladder_message(player)

        self.new_move_allowed(player)

    def new_move_allowed(self, player):
        if self.max_turns == player.turn:
            print("No More Moves Left !! Better luck next time")
            self.end_game()
        print(
            f"{player.name} more {self.max_turns - player.turn} moves left to win. Hurry !!"
        )

    def get_dice_value(self, player, dice):
        input(
            "\n"
            + player.name
            + ": "
            + random.choice(player_turn_text)
            + " Hit the enter to roll dice: "
        )
        print("\nRolling dice...")
        return dice.get_rolled_dice_value()

    def end_game(self):
        sys.exit(0)


def start_game():
    game = SnakeGame(SNAKES, LADDERS, MAX_VAL, MAX_TURNS)
    game.print_welcome_message()
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    player1 = Player()
    player1.get_set_player_name()
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    dice = Dice(DICE_CHOICE)
    dice.set_selected_dice()

    while True:
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        game.get_dice_value(player1, dice)
        game.snake_ladder(player1, dice.current_dice_value)

        is_win = game.check_if_player_win(player1)
        if is_win:
            print("Congratulations You Won")
            game.end_game()


if __name__ == "__main__":
    start_game()