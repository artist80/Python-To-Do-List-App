from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append({'task': task, 'done': False})
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    if request.method == 'POST':
        tasks[task_id]['task'] = request.form['task']
        return redirect(url_for('index'))
    return render_template('update_task.html', task=tasks[task_id])

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    del tasks[task_id]
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    tasks[task_id]['done'] = not tasks[task_id]['done']
    return redirect(url_for('index'))

@app.route('/clear_completed', methods=['POST'])
def clear_completed():
    global tasks
    tasks = [task for task in tasks if not task['done']]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
