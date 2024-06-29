## To-Do List App

A simple and interactive To-Do List application built with Python (Flask) and styled using HTML and CSS. This application allows users to add, update, delete, and mark tasks as completed. 

### Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as completed or uncompleted
- Clear all completed tasks

### Project Structure

```
to_do_list_app/
│
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_task.html
│   ├── update_task.html
├── static/
│   ├── css/
│       ├── styles.css
```

### Getting Started

Follow these steps to get the project up and running on your local machine.

#### Prerequisites

- Python 3.x
- Flask

#### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/to_do_list_app.git
   cd to_do_list_app
   ```

2. **Install Flask:**

   ```bash
   pip install flask
   ```

3. **Run the application:**

   ```bash
   python app.py
   ```

4. **Open your browser and navigate to:**

   ```
   http://127.0.0.1:5000/
   ```

### File Descriptions

- **app.py:** The main Python file that contains the Flask application code.
- **templates/**: Directory containing HTML templates.
  - **base.html:** The base template containing the header, footer, and main layout.
  - **index.html:** The home page displaying the list of tasks.
  - **add_task.html:** The page for adding new tasks.
  - **update_task.html:** The page for updating existing tasks.
- **static/css/**: Directory containing CSS files.
  - **styles.css:** The main stylesheet for styling the web interface.

### Usage

- **Home Page:** View all tasks, mark them as completed/uncompleted, edit, or delete them.
- **Add Task:** Navigate to the 'Add Task' page from the navigation menu to add a new task.
- **Update Task:** Click the 'Edit' link next to a task to update its description.
- **Delete Task:** Click the 'Delete' link next to a task to remove it.
- **Clear Completed Tasks:** Click the 'Clear Completed Tasks' button below the task list to remove all completed tasks.

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Author

CompcIT - contact@compcit.com

### Acknowledgements

- Flask - The web framework used
- HTML and CSS - For the web interface
