def show_analytics(titles, priorities, done_list):

    total=len(titles)
    if total==0:
        print("No tasks.")
        return
    done=0
    pending=0
    low=0
    medium=0
    high=0

    for i in range(len(titles)):
    
        if done_list[i]=="yes":
            done=done+1
        else:
            pending=pending+1
        if priorities[i].lower()=="low":
            low=low + 1
        elif priorities[i].lower()=="medium":
            medium=medium + 1
        elif priorities[i].lower()=="high":
            high=high+1

    percentage=(done / total)*100

    print("\n----- ANALYTICS -----")
    print("Total tasks:", total)
    print("Done:", done)
    print("Pending:", pending)

    print("Completion:", round(percentage, 2), "%")

    print("\nPriority:")
    print("Low:", low)
    print("Medium:", medium)
    print("High:", high)
