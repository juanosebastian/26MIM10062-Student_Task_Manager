# Statement: Student Task Manager

## Problem Statement

Juggling assignments, project deadlines, and subject coursework can get overwhelming fast. When tasks are scattered across different notebooks or apps, it is far too easy to lose sight of upcoming deadlines or misplace track of what is already finished.

At the same time, most commercial task management tools feel overly bloated for basic student needs. They usually require account sign-ups, an active internet connection, and are packed with complex features that end up going unused. What students actually need is something lightweight, fast, and straightforward—a tool that lets them record tasks, set priorities, search through their workload, and track their progress without any fuss.

This project is a solution to that problem: a simple, command-line task manager built in Python that works offline and saves your tasks locally between sessions.

## Scope of the Project

**In Scope**

- Adding, viewing, and deleting tasks
- Assigning titles, priorities (Low, Medium, High), and due dates
- Toggling task status between pending and completed
- Searching tasks by keyword
- Filtering tasks by priority level or completion status
- Displaying quick analytics, including overall completion percentages and priority breakdowns
- Automatically persisting task data to a local text file (`tasks.txt`) across sessions

**Out of Scope**

- Graphical (GUI) or web interfaces
- Multi-user support, cloud syncing, or account management
- Push notifications or deadline reminders
- Recurring tasks and calendar integrations

The scope is intentionally focused on building a rock-solid, reliable core foundation without unnecessary clutter.

## Target Audience

- **Students** balancing coursework, assignments, and deadlines across multiple subjects.
- **Terminal enthusiasts** who prefer rapid, keyboard-driven tools over heavy desktop or web applications.
- **Privacy-conscious users** looking for a zero-setup, fully offline task tracking solution.

## Key Features

- **Core Task Management:** Effortlessly add, review, update status, and remove tasks.
- **Data Persistence:** Automatically load and save your workspace to `tasks.txt`.
- **Search & Filter:** Instantly locate tasks by keyword, status, or priority.
- **Progress Insights:** View completion rates and task breakdowns at a glance.
- **Interactive CLI:** Simple, menu-driven navigation using clear numerical prompts.

---

**Repository:** https://github.com/juanosebastian/26MIM10062-Student_Task_Manager