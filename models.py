from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    text = Column(String(50), unique=True)
    done = Column(Boolean)

    def __init__(self, text=None, done=None):
        self.text = text
        self.done = done

    def __repr__(self):
        return f'<Todo {self.text!r} checked="{self.done!r}">'
