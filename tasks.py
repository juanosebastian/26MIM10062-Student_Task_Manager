def add_task(titles, priorities, due_dates, done_list):

    title=input("Task name: ")
    priority=input("Priority (Low/Medium/High): ")
    due=input("Due date (DD-MM-YYYY): ")

    if due=="":
        due="none"
    titles.append(title)
    priorities.append(priority)
    due_dates.append(due)
    done_list.append("no")
    print("Task added")

def view_tasks(titles, priorities, due_dates, done_list):
    if len(titles)==0:
        print("No tasks.")
        return
    for i in range(len(titles)):
        if done_list[i]=="yes":
            status="Done"
        else:
            status = "Pending"
        print(i+1,"|",titles[i],"|",priorities[i],"|",due_dates[i],"|",status)

def mark_task(titles, done_list):
    if len(titles)==0:
        print("No tasks")
        return

    for i in range(len(titles)):
        print(i+1,"|",titles[i])

    number=int(input("Enter task number: "))
    index=number-1
    if done_list[index]=="no":
        done_list[index]="yes"
        print("Task completed!")
    else:
        done_list[index]="no"
        print("Task marked pending.")

def delete_task(titles, priorities, due_dates, done_list):
    if len(titles)==0:
        print("No tasks.")
        return
    
    for i in range(len(titles)):
        print(i+1,"|",titles[i])

    number = int(input("Enter task number to delete: "))
    index = number - 1
    titles.pop(index)
    priorities.pop(index)
    due_dates.pop(index)
    done_list.pop(index)

    print("Task deleted!")
