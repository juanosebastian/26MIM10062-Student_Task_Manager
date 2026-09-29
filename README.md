# 26MIM10062-Student_Task_Manager

A simple CLI Python program I built to keep track of assignments, deadlines, and project tasks without needing fancy apps or a constant internet connection.

## Why I Built This

Keeping track of deadlines across different subjects can get messy quickly. I wanted something super lightweight that runs directly in the terminal where I can quickly add tasks, set priorities, search through my list, and see how much work I've actually completed. 

## Features

* **Task Management:** Add new tasks, view them in a clean list, mark them complete/pending, or delete them when you're done.
* **Auto-Save:** Saves all your tasks to a local text file (`tasks.txt`), so your data stays saved between sessions.
* **Search & Filter:** Find tasks by keyword, or filter by priority (Low, Medium, High) or status (Done vs Pending).
* **Stats & Analytics:** Computes overall completion percentage and shows a simple breakdown of tasks by priority level.

## Files in this Repo

* `main.py` - The main menu loop that brings everything together.
* `tasks.py` - Handles core task operations like adding, viewing, toggling status, and deleting.
* `storage.py` - Reads from and writes to `tasks.txt`.
* `search.py` - Contains the logic for keyword searching and filtering.
* `analytics.py` - Calculates completion percentages and priority stats.
* `tasks.txt` - Plain text storage file for saving task entries.

## Getting Started

### Prerequisites
You just need Python 3 installed on your computer.

### Running the App

1. Clone or download this repository:
   ```bash
   git clone https://github.com/juanosebastian/26MIM10062-Student_Task_Manager.git
   ```
   
2. Navigate to the project folder
   ```
   cd main
   ```
   
4. Make sure `tasks.txt` is in the same directory (create an empty `tasks.txt` file if it isn't there).

5. Run `main.py`:
   ```bash
   python main.py
   ```

## How to Use It

When you launch `main.py`, just pick an option from 1 to 9:

1. **View tasks:** See all current tasks, their priorities, due dates, and status.
2. **Add task:** Enter a title, set priority (Low/Medium/High), and add a due date.
3. **Mark done/pending:** Change a task status between pending and done.
4. **Delete task:** Remove a task by typing its number.
5. **Search task:** Type a keyword to quickly find matching tasks.
6. **Filter by priority:** Show tasks filtered by Low, Medium, or High priority.
7. **Filter by status:** Show only finished or pending tasks.
8. **Analytics:** Check your task completion rate and priority count.
9. **Exit:** Saves your progress and closes the program.
