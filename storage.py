filename = "tasks.txt"


def load_tasks(titles, priorities, due_dates, done_list):
    f = open(filename, "r")

    for line in f:
        data = line.strip().split(",")

        titles.append(data[0])
        priorities.append(data[1])
        due_dates.append(data[2])
        done_list.append(data[3])
    f.close()


def save_tasks(titles, priorities, due_dates, done_list):

    f = open(filename, "w")

    for i in range(len(titles)):
        f.write(
            titles[i] + "," +
            priorities[i] + "," +
            due_dates[i] + "," +
            done_list[i] + "\n"
        )

    f.close()
