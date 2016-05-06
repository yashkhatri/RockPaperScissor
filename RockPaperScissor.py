__author__ = "Yash Khatri, Sudipta Mallick Das and Martina Öqvist"

import random

rounds_count = 1
win_count = 0
lose_count = 0
result = 0


class Weapon:
    def __str__(self):
        return self.__class__.__name__
    @staticmethod
    def attack(weapon1, weapon2):
        return weapon1.attack(weapon2)


class Rock(Weapon):
    def __init__(self):
        self.name = "rock"

    def attack(self, other):
        return other.attack_by_rock(self)

    def attack_by_rock(self, other):
        return 0

    def attack_by_paper(self, other):
        return 1

    def attack_by_scissor(self, other):
        return -1


class Paper(Weapon):
    def __init__(self):
        self.name = "paper"

    def attack(self, other):
        return other.attack_by_paper(self)

    def attack_by_rock(self, other):
        return -1

    def attack_by_paper(self, other):
        return 0

    def attack_by_scissor(self, other):
        return 1


class Scissor(Weapon):
    def __init__(self):
        self.name = "scissor"

    def attack(self, other):
        return other.attack_by_scissor(self)

    def attack_by_rock(self, other):
        return 1

    def attack_by_paper(self, other):
        return -1

    def attack_by_scissor(self, other):
        return 0


class Adversary:
    def computer_input(self):
        r_num = random.randint(1, 3)
        if r_num == 1:
            return Rock()
        elif r_num == 2:
            return Paper()
        else:
            return Scissor()


class User:
    def user_input(self):
        global rounds_count
        print("Make your choice for round", rounds_count, ": (rock|r, paper|p, scissor|s)")
        choice = input().lower()
        if choice == "r" or choice == "rock":
            return Rock()
        elif choice == "p" or choice == "paper":
            return Paper()
        elif choice == "s" or choice == "scissor":
            return Scissor()
        else:
            print("Invalid choice.")
            self.user_input()


def fight(weapon1, weapon2):
    global result
    result = Weapon.attack(weapon1, weapon2)
    global win_count
    global lose_count
    if result > 0:
        print("You choose", weapon1, ", your opponent chose", weapon2, ". You win!")
        win_count += 1
    elif result == 0:
        print("You choose", weapon1, ", your opponent chose", weapon2, ". It's a tie!")
    else:
        print("You choose", weapon1, ", your opponent chose", weapon2, ". Your opponent wins!")
        lose_count += 1


def show_results():
    global win_count
    global lose_count
    if lose_count == win_count:
        print("Result: You won", win_count, "time, your opponent won", lose_count, "time. It's a tie!")
    elif lose_count > win_count:
        print("Result: You won", win_count, "time, your opponent won", lose_count, "time. Your opponent wins!")
    else:
        print("Result: You won", win_count, "time, your opponent won", lose_count, "time. You win!")


def run():
    global rounds_count
    total_rounds = input("How many rounds? ")
    try:
        int(total_rounds)
        user = User()
        comp = Adversary()
        while rounds_count <= int(total_rounds):
            user = user.user_input()
            adversary = comp.computer_input()
            fight(user, adversary)
            rounds_count += 1
    except ValueError:
        print("Illegal input. Declare number of rounds in a number.")
        run()


run()
show_results()
