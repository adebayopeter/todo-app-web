import streamlit as st
from modules.functions import get_todos, write_todos

todos = get_todos()


def add_todo():
    new_todo_input = st.session_state["new_todo"] + "\n"
    todos.append(new_todo_input)
    write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for idx, todo in enumerate(todos):
    checkbox_id = f"{todo}-{idx}"
    checkbox = st.checkbox(todo, key=checkbox_id)
    if checkbox:
        todos.pop(idx)
        write_todos(todos)
        del st.session_state[checkbox_id]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
