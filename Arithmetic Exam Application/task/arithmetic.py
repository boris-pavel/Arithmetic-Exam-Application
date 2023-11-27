import random

operations = ("+", "-", "*")
tasks_num = 5  # number of tasks in the exam
points = 0  # number of points accumulated


def evaluate(a, b, sign):
    if sign == '-':
        return a - b
    elif sign == '+':
        return a + b
    else:
        return a * b


def get_difficulty():
    difficulty_level = 0
    while difficulty_level != 1 or difficulty_level != 2:
        try:
            difficulty_level = int(input("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
"""))
            if difficulty_level != 1 and difficulty_level != 2:
                print("Incorrect format.")
                continue
            else:
                return difficulty_level
        except ValueError:
            print("Incorrect format.")


def produce_task(difficulty_level):
    match difficulty_level:
        case 1:
            num1 = random.randint(2, 9)
            num2 = random.randint(2, 9)
            op = random.choice(operations)
            return f"{num1} {op} {num2}"
        case 2:
            return f"{random.randint(11, 29)}"


def input_answer():
    try:
        ans = int(input())
        return ans
    except ValueError:
        print("Incorrect format.")
        return False


def verify_answer(difficulty, task, answer):
    match difficulty:
        case 1:
            return True if evaluate(int(task[0]), int(task[4]), task[2]) == answer else False
        case 2:
            return True if int(task) * int(task) == answer else False


difficulty = get_difficulty()
while tasks_num > 0:
    task = produce_task(difficulty)
    print(task)

    answer = input_answer()
    while isinstance(answer, bool):  # while answer is in incorrect format
        print(task)
        answer = input_answer()
    tasks_num -= 1

    if verify_answer(difficulty, task, answer):
        print("Right!")
        points += 1
    else:
        print("Wrong!")

print(f"Your mark is {points}/5.")

save_result = input("Would you like to save your result to the file? Enter yes or no.\n")
level_description = ""

match difficulty:
    case 1:
        level_description = "(simple operations with numbers 2-9)"
    case 2:
        level_description = "(integral squares of 11-29)"

match save_result:
    case "yes" | "YES" | "y" | "Yes":
        username = input("What is your name?\n")
        file = open("results.txt", 'a')
        file.write(f"{username}: {points}/5 in level {difficulty} {level_description}\n")
        file.close()
        print("The results are saved in \"results.txt\".")
    case _:
        exit()
