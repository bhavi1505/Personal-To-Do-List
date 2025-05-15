import json
from colorama import init, Fore, Style

init(autoreset=True)  # Automatically reset colors after each print

class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

def display_tasks(tasks):
    if not tasks:
        print("  (none)")
        return
    for i, task in enumerate(tasks, 1):
        status = Fore.GREEN + "✔" if task.completed else Fore.RED + "✘"
        color = Fore.GREEN if task.completed else Fore.RED
        print(f"{i}. [{status}{Fore.RESET}] {color}{task.title}{Fore.RESET} - {task.category}")
        print(f"   {Style.DIM}{task.description}{Style.RESET_ALL}")

def main():
    tasks = load_tasks()
    while True:
        print(Fore.YELLOW + "\n--- Personal To-Do List ---" + Fore.RESET)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Save & Exit")
        print("6. View Completed Tasks")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category (e.g., Work, Personal): ")
            tasks.append(Task(title, description, category))
            print(Fore.GREEN + "✅ Task added!")

        elif choice == '2':
            incomplete_tasks = [task for task in tasks if not task.completed]
            completed_tasks = [task for task in tasks if task.completed]

            print(Fore.YELLOW + "\n--- Incomplete Tasks ---")
            display_tasks(incomplete_tasks)

            print(Fore.YELLOW + "\n--- Completed Tasks ---")
            display_tasks(completed_tasks)

        elif choice == '3':
            display_tasks(tasks)
            try:
                num = int(input("Enter task number to mark completed: ")) - 1
                tasks[num].mark_completed()
                print(Fore.GREEN + f"✅ Task '{tasks[num].title}' marked as completed!")
            except (ValueError, IndexError):
                print(Fore.RED + "❌ Invalid task number.")

        elif choice == '4':
            display_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: ")) - 1
                print(Fore.RED + f"🗑️ Task '{tasks[num].title}' deleted.")
                del tasks[num]
            except (ValueError, IndexError):
                print(Fore.RED + "❌ Invalid task number.")

        elif choice == '5':
            save_tasks(tasks)
            print(Fore.CYAN + "📁 Tasks saved. Goodbye!")
            break

        elif choice == '6':
            completed = [t for t in tasks if t.completed]
            if completed:
                print(Fore.YELLOW + "\n--- Completed Tasks ---")
                display_tasks(completed)
            else:
                print(Fore.RED + "❌ No tasks marked as completed.")

        else:
            print(Fore.RED + "❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
