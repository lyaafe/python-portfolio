
import emoji
from random import randint


def hoop_game():
    print(emoji.emojize(":fire: Let's go to hoop game :fire:"))

    while True:
        times = int(input(emoji.emojize(":alarm_clock: How many times do you want to play? ")))

        for _ in range(times):
            num = int(input("What is your number? "))

            n = 0
            while n < num:
                n += 1

                if n % 3 == 0:
                    print("hoop")
                    continue

                print(n)

        again = input("Do you want to play again? (yes/no): ")

        if again == "no":
            break


def dice_game():
    print(emoji.emojize(":game_die: Welcome to toss game :game_die:"))

    while True:
        times = int(input(emoji.emojize(":alarm_clock: How many times do you want to play? ")))

        for _ in range(times):
            answer = randint(1, 6)
            guess = int(input("Tell your number (1-6): "))

            if guess == answer:
                print("Wow! Great guess ")
            else:
                print(
                    emoji.emojize(
                        f"My answer is {answer} :game_die:"
                    )
                )

        again = input("Do you want to play again? (yes/no): ")

        if again == "no":
            break


class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Cannot divide by zero"
        return self.a / self.b

    def exponent(self):
        return self.a ** self.b


def calculator():
    while True:

        menu = input(
            "\n"
            "1: Sum\n"
            "2: Subtract\n"
            "3: Multiply\n"
            "4: Divide\n"
            "5: Exponent\n"
            "6: Exit\n"
            "Choose: "
        )

        if menu == "6":
            print(emoji.emojize("Thanks for using calculator :red_heart:"))
            break

        if menu not in ("1", "2", "3", "4", "5"):
            print("Invalid choice!")
            continue

        a = float(input("Number 1: "))
        b = float(input("Number 2: "))

        cal = Calculator(a, b)

        if menu == "1":
            print(cal.sum())

        elif menu == "2":
            print(cal.subtract())

        elif menu == "3":
            print(cal.multiply())

        elif menu == "4":
            print(cal.divide())

        elif menu == "5":
            print(cal.exponent())


def games():
    while True:

        print(emoji.emojize(":fire: Let's play funny games :fire:"))

        choice = input(emoji.emojize(
            "Which game do you like?\n"
            "1: Hoop :fire:\n"
            "2: Toss :game_die:\n"
            "3: Exit :door:\n"
            "Choose: ")
        )

        if choice == "1":
            hoop_game()

        elif choice == "2":
            dice_game()

        elif choice == "3":
            break

        else:
            print("Invalid choice!")


def main():

    name = input(
        emoji.emojize(" :red_heart: What is your name? : ")
    )

    while True:

        menu = input(
            emoji.emojize(
                f"\nHello {name} :red_heart:\n"
                "Please choose one item:\n"
                "1: Game :video_game:\n"
                "2: Calculator :abacus:\n"
                "3: Exit :door:\n"
                "Choose: "
            )
        )

        if menu == "1":
            games()

        elif menu == "2":
            calculator()

        elif menu == "3":
            print(
                emoji.emojize(
                    f"Thanks {name} :red_heart:"
                )
            )
            break

        else:
            print("Invalid choice!")


main()    