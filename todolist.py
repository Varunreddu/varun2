from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    if task_content.strip():  # Ensure task is not empty or just spaces
        tasks.append({"content": task_content.strip(), "completed": False})
    return redirect(url_for('index'))

@app.route('/complete/<int:task_index>')
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:task_index>')
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)  # 'pop' is cleaner for deletion
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
