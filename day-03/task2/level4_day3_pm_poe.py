#program register.py

def add_learner(learners, number, name):
    if number in learners:
        return False
    learners[number] = {"name": name, "marks": []}
    return True

def add_mark(learners, number, mark):
    if number not in learners:
        return False
    learners[number]["marks"].append(mark)
    return True

def rename_learner(learners, number, new_name):
    if number not in learners:
        return False
    learners[number]["name"] = new_name
    return True

def delete_learner(learners, number):
    if number not in learners:
        return False
    del learners[number]
    return True

def find_by_name(learners, text):
    matches = []
    for number in learners:
        if text.lower() in learners[number]["name"].lower():
            matches.append(number)
    return matches

def average_of(values):
    total = 0
    for v in values:
        total = total + v
    return total / len(values)

def learner_average(learners, number):
    marks = learners[number]["marks"]
    if len(marks) == 0:
        return None
    return average_of(marks)

def ranking(learners):
    rows = []
    for number in learners:
        avg = learner_average(learners, number)
        if avg is not None:
            rows.append((avg, number))
    n = len(rows)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if rows[j][0] < rows[j + 1][0]:
                rows[j], rows[j + 1] = rows[j + 1], rows[j]
    return rows

def print_ranking(learners):
    rows = ranking(learners)
    if len(rows) == 0:
        print("No marks captured yet.")
        return
    print("Rank  Number    Name          Average")
    for position in range(len(rows)):
        avg = rows[position][0]
        number = rows[position][1]
        name = learners[number]["name"]
        print(f"{position + 1:<6}{number:<10}{name:<14}{avg:>6.1f}")

def is_valid_number(text):
    return text.isdigit() and len(text) == 7

def is_valid_mark(text):
    return text.isdigit() and int(text) <= 100

def show_menu():
    print()
    print("1. Add learner")
    print("2. Add mark")
    print("3. Rename learner")
    print("4. Delete learner")
    print("5. Find by name")
    print("6. Show ranking")
    print("7. Exit")

def ask_number():
    return input("Student number (7 digits): ")

def main():
    learners = {}
    choice = ""
    while choice != "7":
        show_menu()
        choice = input("Choice: ")
        if choice == "1":
            number = ask_number()
            name = input("Name: ")
            if not is_valid_number(number) or name == "":
                print("Invalid number or name.")
            elif add_learner(learners, number, name):
                print("Added.")
            else:
                print("That student number already exists.")
        elif choice == "2":
            number = ask_number()
            text = input("Mark (0-100): ")
            if not is_valid_mark(text):
                print("Invalid mark.")
            elif add_mark(learners, number, int(text)):
                print("Mark added.")
            else:
                print("No such learner.")
        elif choice == "3":
            number = ask_number()
            if rename_learner(learners, number, input("New name: ")):
                print("Renamed.")
            else:
                print("No such learner.")
        elif choice == "4":
            if delete_learner(learners, ask_number()):
                print("Deleted.")
            else:
                print("No such learner.")
        elif choice == "5":
            found = find_by_name(learners, input("Name contains: "))
            if len(found) == 0:
                print("No match.")
            for number in found:
                print(number, learners[number]["name"], learners[number]["marks"])
        elif choice == "6":
            print_ranking(learners)
        elif choice == "7":
            print("Goodbye.")
        else:
            print("Invalid choice. Enter 1 to 7.")

main()

