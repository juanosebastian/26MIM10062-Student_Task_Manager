def search_tasks(titles, priorities, due_dates, done_list):

    keyword=input("Enter task name to search: ")
    found=False
    for i in range(len(titles)):
        if keyword.lower() in titles[i].lower():
            print(i + 1,"|",titles[i],"|",priorities[i],"|",due_dates[i])
            found=True
    if found==False:
        print("No task found.")

def filter_priority(titles, priorities, due_dates):
    priority=input("Enter priority (Low/Medium/High): ")
    found=False
    for i in range(len(titles)):
        if priorities[i].lower()==priority.lower():
            print(i + 1,"|",titles[i],"|",priorities[i],"|",due_dates[i])
            found = True
    if found==False:
        print("No tasks with that priority.")

def filter_status(titles, done_list):
    print("1. Pending")
    print("2. Done")
    choice=input("Choose: ")
    for i in range(len(titles)):
        if choice=="1" and done_list[i]=="no":
            print(i + 1, "|", titles[i])
        elif choice == "2" and done_list[i] == "yes":
            print(i + 1, "|", titles[i])
