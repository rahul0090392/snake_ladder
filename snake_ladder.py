import time
import random
import sys
from constant import (
    SLEEP_BETWEEN_ACTIONS,
    MAX_VAL,
    VALID_DICE,
    CROOKED_DICE,
    DICE_CHOICE,
    SNAKES,
    LADDERS,
    player_turn_text,
    snake_bite,
    ladder_jump,
)


class Player:
    def __init__(self, current_position, turn, name):
        self.current_position = 0
        self.turn = 0
        self.name = name

    def update_position(self, current_position):
        self.current_position = current_position

    def increment_turn(self):
        self.turn += 1


class Dice:
    def __init__(self, dices):
        self.dices = dices

    def set_selected_dice(self, selected_dice):
        self.selected_dice = None

        while self.selected_dice not in self.dices.keys():
            print("We have two types of dice availabe \n1. Common \n 2. Cooked \n")
            self.selected_dice = input(" Please Enter your selected dice: ").strip()

        self.selected_dice = self.dices[selected_dice]

    def get_rolled_dice_value(self):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        dice_value = random.choice(self.selected_dice)
        print("Its a " + str(dice_value))
        return dice_value


class SnakeGame:
    def __init__(self, snakes, laddeers, max_value):
        self.snakes = SNAKES
        self.laddeers = LADDERS
        self.max_value = MAX_VAL

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

    def set_player(self, player_obj):
        self.player = player_obj


if __name__ == "__main__":
    start()