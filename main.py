from flask import Flask, request, jsonify, render_template, redirect
import sqlite3
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='logs/app.log',
    filemode='a',
    datefmt='%Y-%m-%d %H:%M:%S'
)



app = Flask(__name__)
DB_File = "task.do"


@app.route("/ping")
def ping():
    return "pong", 200

@app.route("/", methods=['GET'])
def home():
    try:
        with sqlite3.connect(DB_File) as conn:
            cursor = conn.execute("SELECT * FROM tasks")
            tasks = [{"id":row[0], 'task':row[1]} for row in cursor.fetchall()]
        logging.info("Featched all logs successfully.")
        return render_template("index.html", tasks=tasks)
    except Exception as e:
        logging.error(f"Error fetching the details: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

#initializing the database
def int_db():
    with sqlite3.connect(DB_File) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     task TEXT NOT NULL
                     )""")
        
    logging.info("Created the database")
        


#Get response for all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    try:
        with sqlite3.connect(DB_File) as conn:
            cursor = conn.execute("SELECT * FROM tasks")
            tasks = [{"id":row[0], 'task':row[1]} for row in cursor.fetchall()]
        logging.info("Featched all logs successfully.")
        return jsonify(tasks)
    except Exception as e:
        logging.error(f"Error fetching the details: {e}")
        return jsonify({"error": "Internal Server Error"}), 500
    

@app.route("/reset_ids", methods=["POST"])
def reset_ids():
    try:
        with sqlite3.connect(DB_File) as conn:
            cursor = conn.execute("SELECT COUNT(*) FROM tasks")
            count = cursor.fetchone()[0]
            if count == 0:
                conn.execute("DELETE FROM sqlite_sequence WHERE name='tasks'")
                logging.info("Task ID counter reset to 1.")
                return "ID counter reset", 200
            else:
                return "Cannot reset — tasks table is not empty.", 400
    except Exception as e:
        logging.error(f"Error resetting ID counter: {e}")
        return "Internal Server Error", 500



        
#Add a new task
@app.route("/add", methods=["POST"])
def add_task():
    try:
        if request.is_json:
            task = request.json.get("task")
        else:
            task = request.form.get("task")
        if not task:
            return jsonify({"error": "Task content are required."}), 400
        with sqlite3.connect(DB_File) as conn:
            cursor = conn.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
            task_id = cursor.lastrowid
        logging.info(f"New task added with task id - {task_id}")
        if request.is_json:
            return jsonify({"id": task_id, "task": task})
        else:
            return redirect("/")
    except Exception as e:
        logging.error(f"Error while adding new task: {e}")
        return jsonify({"error": "Internal Server Error"}), 500



#Update task
@app.route("/update/<int:id>", methods=["PUT"]) 
def update_task(id):
    try:
        task = request.json.get("task")
        if not task:
            return jsonify({"error": "Task content are required."}), 400
        with sqlite3.connect(DB_File) as conn:
            conn.execute("UPDATE tasks SET task = ? WHERE id = ?", (task, id))
        logging.info(f"Task details has been updated - {id}")
        return jsonify({"message": "Task Updated"})
    except Exception as e:
        logging.error(f"Error while updating the table: {e}")
        return jsonify({"error": "Internal Server Error"}), 500



#Delete task
@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_task(id):
    try:
        with sqlite3.connect(DB_File) as conn:
            conn.execute("DELETE FROM tasks WHERE id = ?", (id,))
        logging.info(f"Task details has been deleted - {id}")
        return jsonify({"message": "Task deleted"})
    except Exception as e:
        logging.error(f"Error while deleting the task {id}: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    int_db()
    app.run(debug=True, host = "0.0.0.0", port=5000)

