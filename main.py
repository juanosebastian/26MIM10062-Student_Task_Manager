import tasks
import storage
import search
import analytics

titles = []
priorities = []
due_dates = []
done_list = []

storage.load_tasks(titles , priorities , due_dates , done_list)

while True:
    print("\n")
    print("===== STUDENT TASK MANAGER =====")

    print("1. View tasks")
    print("2. Add task")
    print("3. Mark done/pending")
    print("4. Delete task")
    print("5. Search task")
    print("6. Filter by priority")
    print("7. Filter by status")
    print("8. Analytics")
    print("9. Exit")

    choice = input("Choose an option: ")

    if choice=="1":
        tasks.view_tasks(titles , priorities , due_dates , done_list)

    elif choice=="2":
        tasks.add_task(titles , priorities , due_dates , done_list)
        storage.save_tasks(titles , priorities , due_dates , done_list)

    elif choice == "3":
        tasks.mark_task(titles , done_list)
        storage.save_tasks(titles , priorities , due_dates , done_list)

    elif choice == "4":
        tasks.delete_task(titles , priorities , due_dates , done_list)
        storage.save_tasks(titles , priorities , due_dates , done_list)

    elif choice == "5":
        search.search_tasks(titles , priorities , due_dates , done_list)

    elif choice == "6":
        search.filter_priority( titles, priorities, due_dates)

    elif choice == "7":
        search.filter_status(titles, done_list)
    elif choice == "8":
        analytics.show_analytics(titles, priorities, done_list)
    elif choice == "9":
        storage.save_tasks(titles , priorities , due_dates , done_list)

        print("Tasks saved.")
        break

    else:
        print("Invalid option.")
