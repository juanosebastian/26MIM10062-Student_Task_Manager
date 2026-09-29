# Statement: Student Task Manager

## Problem Statement

It's easy for the number of assignments, project deadlines, and subjects to become overwhelming. If the tasks are spread out among different notebooks or apps, you soon lose sight of the deadlines that are coming up or end up losing track of those that have already been completed.

At the same time, the majority of commercial task management tools appear to be far too complicated for the simple needs of students. These tools generally demand that users sign up for an account, have an active internet connection, and include a large number of complicated features most of which are never used. All that students really need is something light, quick, and simple—a tool which enables them to record tasks, assign priorities, search their workload and keep track of their progress without any trouble.

This project provides a solution to that problem: it is a simple task manager designed for use from the command line, written in Python, and which functions offline by saving your tasks locally between sessions.

## Scope of the Project

**In Scope**

- Adding, viewing, and deleting tasks
- Assigning titles, priorities (Low, Medium, High), and due dates
- Toggling task status between pending and completed
- Searching tasks by keyword
- Filtering tasks by priority level or completion status
- Displaying quick analytics, including overall completion percentages and priority breakdowns
- Automatically saving task data to a local text file (`tasks.txt`) between sessions.

**Out of Scope**

- Graphical (GUI) or web interfaces
- Multi-user support, cloud syncing, or account management
- Push notifications or deadline reminders
- Recurring tasks and calendar integrations

On purpose the scope is centered on establishing a firm and reliable core foundation without including unnecessary elements.

## Target Audience

- Students managing their coursework, assignments, and deadlines for a number of subjects.
- People who are keen on terminals and prefer fast, keyboard-based tools to more resource-intensive desktop or web applications.
- For users who care about their privacy and want a task tracking solution that requires no setup and works completely offline.

## Key Features

– You can easily add, check over, update the status of, and delete tasks.
– **Data Persistence:** The system will automatically load and save your workspace into a file called tasks.txt.
- **Search & Filter:** You can immediately find tasks by using a keyword, status, or priority.
- **Progress Insights:** You can get an at-a-glance view of the completion rates and the breakdown of tasks.
- **Interactive command-line interface:** This features easy navigation through a menu using straightforward numerical prompts.

---

**Repository:** https://github.com/juanosebastian/26MIM10062-Student_Task_Manager
