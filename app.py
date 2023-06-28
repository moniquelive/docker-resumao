from flask import Flask, render_template, url_for, redirect, request

from database import db_session, init_db
from models import Todo

app = Flask(__name__)
init_db()


@app.route("/")
def home():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)


@app.route("/item", methods=["POST"])
def new_item():
    text = request.form.get('text', '')
    done = request.form.get('done', '') == 'on'
    todo = Todo(text, done)

    db_session.add(todo)
    db_session.commit()
    return redirect(url_for('home'))


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(debug=True)
