from base import Base
from task import TaskManager
from advisor import Advisor
import time
def game_initialization():
    print("\n==============================")
    print("      WELCOME TO MOTHER BASE")
    print("==============================\n")
    time.sleep(1)

    print("Initializing systems...")
    time.sleep(1)
    print("Checking platform integrity...")
    time.sleep(1)
    print("Assigning tactical officer...")
    time.sleep(1.5)

    print("\nFreya: Hello, Boss. Your assigned field advisor and tactical officer reporting for duty.")
    time.sleep(1)

    print("Freya: I will assist you with base management, mission planning, and resource coordination.")
    time.sleep(1)

    print("Freya: As a reminder, we are a private military company, operating independently to fulfill contracts, secure resources, and expand our operational capabilities.")
    time.sleep(2)

    print("Freya: Our success depends on strategic planning, efficient resource use, and precise mission execution.")
    time.sleep(2)

    print("Freya: Before we begin, I recommend that you first check the current construction status of our base and our available funds.")
    time.sleep(2)

    print("Freya: You can take on missions to earn funds, which can then be used to build platforms. Each new platform will improve our mission success rates to some extent.")
    time.sleep(2)

    print("Freya: Also, remember that deploying for missions will cost funds. Please plan and allocate your resources carefully, Boss.")
    time.sleep(2)

    print("\nFreya: For a better world, Boss. Let’s begin.")
    time.sleep(2)

    print("\n==============================\n")
    time.sleep(1)
def main():
    game_initialization()
    base = Base()
    task_manager = TaskManager(base)
    advisor = Advisor()

    while True:
        print("\n### Mother Base Main Console ###")
        print("1. Show Base Status")
        print("2. Show Current Funds")
        print("3. Build Platform")
        print("4. View and Execute Tasks")
        print("5. Ask Freya for Advice")
        print("6. Exit game")

        try:
            raw_input_value = input("Please select an option (1-6): ").strip()
            choice = int(raw_input_value)

            if not 1 <= choice <= 6:
                print('Invalid input, please enter a number between 1 and 6.')
                continue

        except ValueError:
            print('Invalid input, please enter a valid number.')
            continue

        if choice == 1:
            print("")
            time.sleep(1)
            base.show_platfroms_status()
            time.sleep(1)
            base.show_platforms(base.init_platform)
            time.sleep(1)

        elif choice == 2:
            print("")
            
            time.sleep(1)
            print(f"Current Gold: {base.gold} credits.")
            time.sleep(1)
            print(advisor.advise_on_money(base))
            time.sleep(1)



        elif choice == 3:
            print("")
            
            time.sleep(1)
            base.run_build_menu()
            time.sleep(1)
            print(advisor.advise_on_build(base))
            time.sleep(1)

        elif choice == 4:
            print("")
            time.sleep(1)
            tasks = task_manager.task_list()

            print("\nAvailable Tasks:")
            for i, task in enumerate(tasks):
                print(f'{i + 1}. [{task.tier.upper()}] {task.name} - Cost: {task.cost}, Reward: {task.reward}, Success Rate: {task.success_rate:.2f}')

            task_choice = input("Select a task number (or Q to cancel): ").strip()
            if task_choice.upper() == 'Q':
                continue

            if not task_choice.isdigit():
                print("Invalid choice. Please enter a valid task number.")
                continue

            task_index = int(task_choice) - 1
            
            if task_index < 0 or task_index >= len(tasks):
                print("Invalid choice. Please select a number from the list.")
                continue

            selected_task = tasks[task_index]

            #advisor
            print("")
            time.sleep(1)

            print(advisor.advise_on_task(selected_task))
            time.sleep(1)
            print("")
            time.sleep(1)
            print(advisor.advise_on_success_rate(selected_task))
            print("")

            confirm = input(f"{advisor.name}: Boss, do you confirm this mission? (Y/N): ").strip().upper()
            if confirm != 'Y':
                time.sleep(1)
                print(f"{advisor.name}: Understood, Boss. Returning to Main Console.")
                continue
            
            reward = selected_task.mission_start(base)

            if reward:
                base.gold += reward
                print(f"[INFO] Reward collected. New balance: {base.gold} credits.")
                time.sleep(1)

                print(advisor.after_task(True))
                time.sleep(1)
            else:
                print(f"[RESULT] No reward collected. Current balance: {base.gold} credits.")
                time.sleep(1)
                print(advisor.after_task(False))
                time.sleep(1)
        
        
        elif choice == 5:
            print("")
            print("[ADVISOR MODE]")
            print(advisor.advise_on_money(base))

            if advisor.last_task_success is True:
                time.sleep(1)
                print(f"{advisor.name}: We're doing great, Boss! Let's keep up the momentum!")
            elif advisor.last_task_success is False:
                time.sleep(1)
                print(f"{advisor.name}: It's okay, Boss... we'll bounce back!")
            else:
                time.sleep(1)
                print(f"{advisor.name}: Ready for action anytime, Boss!")



        elif choice == 6:
            print("")
            print("Saving progress...")
            print("Exiting game. See you next time, Boss!")
            break

if __name__ == "__main__":
    main()